from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404

from .forms import *
from alumnos.forms import *
from .utils import *
from programa.forms import *
from programa.models import ReinscripcionPrograma,ConstanciaPrograma
from calendarios.models import Calendario
from tesis.forms import *
import ast

#Cancelar solicitud
def solicitud_cancelar(request):
	if request.method == "POST":
		if form_solicitud != None:
			form_solicitud.delete()
		else:
			print("NO hay solicitud")
	return redirect("index")

# INSCRIPCIÓN --------------------------------------------------------------------------------
@login_required
def inscripcion_datos(request):
	global control
	usuario = request.user
	registroP = DatosPersonalesAlumno.objects.filter(cuenta=usuario)
	registroA = DatosAcademicosAlumno.objects.filter(cuenta=usuario)
	if len(registroP)==0:
		registro_solicitud = []
	else:
		registro_solicitud = SolicitudInscripcion.objects.filter(datos_personales=registroP[0])

	if (len(registro_solicitud)>0) and control:
		control = False
		return redirect("failure","1")
	
	if request.method == "GET":
		return render(request,"inscripcion/inscripcionDatos.html",{
			'datosP': registroP[0] if len(registroP) == 1 else "X",
			'datosA': registroA[0] if len(registroA) == 1 else "X",
		})
	try:
		global form_solicitud
		global correo
		new_form_datos_p = actualizar_personales(request,registroP,usuario)
		new_form_datos_a = actualizar_academicos(request,registroA,usuario)
		
		if (len(registro_solicitud)==0):
			new_form_inscripcion = SolicitudInscripcion.objects.create(
				datos_personales = new_form_datos_p,
				datos_academicos = new_form_datos_a,
				fecha = timezone.now()
			)
			form_solicitud = new_form_inscripcion
		else:
			form_solicitud = registro_solicitud[0]
		correo = request.POST["correo_1"]
		control = True
		return redirect('inscripcion_antecedentes')
	except Exception as error:
		return render(request,"inscripcion/inscripcionDatos.html",{
			'datosP': registroP[0] if len(registroP) == 1 else "X",
			'datosA': registroA[0] if len(registroA) == 1 else "X",
			'error': error 
		})

@login_required
def inscripcion_antecedentes(request):
	get_object_or_404(SolicitudInscripcion,pk=form_solicitud.id)
	if request.method == "GET":
		forms_antecedentes = FormsetAntecedentes()
		return render(request,"inscripcion/inscripcionAntecedentes.html",{'formsA': forms_antecedentes})
	try:
		antecedentes = InscripcionAntecedentes.objects.filter(id_solicitud_inscripcion=form_solicitud)
		for antecedente in antecedentes:
			antecedente.id_antecedentes.delete()

		forms_antecedentes = FormsetAntecedentes(request.POST)
		if forms_antecedentes.is_valid():
			for form in forms_antecedentes:
				nivel = form.cleaned_data.get('nivel_academico_cursado')
				programa = form.cleaned_data.get("programa_academico_cursado")
				institucion = form.cleaned_data.get("institucion_donde_curso")
				estado = form.cleaned_data.get("estado_institucion")
				fecha = form.cleaned_data.get("fecha_graduacion")
				form_antecedentes = AntecedentesAcademicos.objects.create(
					nivel_academico_cursado = nivel,
					programa_academico_cursado = programa,
					institucion_donde_curso = institucion,
					estado_institucion = estado,
					fecha_graduacion = fecha
				)
				InscripcionAntecedentes.objects.create(
					id_solicitud_inscripcion = form_solicitud,
					id_antecedentes = form_antecedentes
				)
			return redirect('inscripcion_programa')
		else:
			return render(request,"inscripcionAntecedentes.html",{
				'formsA': forms_antecedentes,
				'error': forms_antecedentes.errors 
			})
	except Exception as error:
		forms_antecedentes = FormsetAntecedentes()
		return render(request,"inscripcionAntecedentes.html",{
			'formsA': forms_antecedentes,
			'error': error 
		})

@login_required
def inscripcion_programa(request):
	get_object_or_404(SolicitudInscripcion,pk=form_solicitud.id)
	if request.method == "GET":
		forms_programa = FormsetProgramaSem()
		return render(request,"inscripcion/inscripcionPrograma.html",{'formsP': forms_programa})
	try:
		programa_borrar = InscripcionPrograma.objects.filter(id_solicitud_inscripcion=form_solicitud)
		for programa in programa_borrar:
			programa.delete()
		forms_programa = FormsetProgramaSem(request.POST)

		if forms_programa.is_valid():
			for form in forms_programa:
				form_programa = form.cleaned_data.get('id_programa_semestral')
				InscripcionPrograma.objects.create(
					id_solicitud_inscripcion = form_solicitud,
					id_programa_semestral = form_programa
				)
		else:
			print(forms_programa.errors)
		return redirect('inscripcion_firmas')
	except Exception as error:
		forms_programa = FormsetProgramaSem()
		return render(request,"inscripcionPrograma.html",{
			'formsP': forms_programa,
			'error': error 
		})
	
@login_required	
def inscripcion_firmas(request):
	global form_solicitud
	usuario = request.user
	if not usuario.is_staff:
		get_object_or_404(SolicitudInscripcion,pk=form_solicitud.id)
	if request.method == 'GET':
		datos = informacion_inscripcion(form_solicitud)
		datos["antecedentes"] = ast.literal_eval(datos["antecedentes"])
		datos["programa"] = ast.literal_eval(datos["programa"])
		return render(request,"firmado/inscripcionFirmas.html",{
			'usuario':usuario,
			'datos': datos,
			'formF':FormSolicitudInscripcion,
			'profes': User.objects.filter(is_staff=True),
		})
	try:
		solicitud = get_object_or_404(SolicitudInscripcion,pk=form_solicitud.id)
		usuario_docente = usuario.username
		if usuario.is_staff:
			if usuario_docente == "Jefe_area":
				solicitud.firma_jefe = True
			if usuario_docente == solicitud.asesor.username:
				solicitud.firma_asesor = True
			solicitud.save()
			form_solicitud = None
			return redirect('success',"3")
		else:
			solicitud = get_object_or_404(SolicitudInscripcion,pk=form_solicitud.id)
			solicitud.asesor = User.objects.get(id=request.POST.get('nombre_asesor'))
			solicitud.jefe = User.objects.get(username='Jefe_area')
			solicitud.firma_alumno = comprueba_firma(request.POST.get("firma_alumno"))
			solicitud.aviso_privacidad = comprueba_firma(request.POST.get("aviso_privacidad"))
			solicitud.save()
			form_solicitud = None
			enviar_correo(solicitud.id,"Solicitud de Inscripción")
			return redirect('success',solicitud.id)
	except Exception as error:
		return render(request,"firmado/inscripcionFirmas.html",{
			'formF':SolicitudInscripcion,
			'profes': User.objects.filter(is_staff=True),
			'error': error
		})

def inscripcion_firmas_pendiente(request):
	if request.method == 'GET':
		usuario = request.user
		if usuario.username == "Jefe_area":
			solicitudes_usuario = SolicitudInscripcion.objects.all()
			pendientes = solicitudes_usuario.filter(firma_jefe = False)|solicitudes_usuario.filter(firma_jefe = None)
			no_pendientes = SolicitudInscripcion.objects.all().filter(firma_jefe = True)
		else:
			solicitudes_usuario = SolicitudInscripcion.objects.filter(asesor=usuario)
			pendientes = solicitudes_usuario.filter(firma_asesor = False)|solicitudes_usuario.filter(firma_asesor = None)
			no_pendientes = SolicitudInscripcion.objects.filter(asesor=usuario).filter(firma_asesor = True)
		return render(request,"firmado/inscripcionFirmasStaff.html",{
			'solicitudesP':pendientes,
			'solicitudesN':no_pendientes,
		})
	try:
		global form_solicitud
		form_solicitud = SolicitudInscripcion.objects.get(id=request.POST.get("solicitud_id"))
		return redirect("inscripcion_firmas")
	except:
		pass

# REINSCRIPCION -------------------------------------------------------------------------------
@login_required
def reinscripcion(request):
	global control
	usuario = request.user
	if not usuario.is_staff:
		registroP = DatosPersonalesAlumno.objects.filter(cuenta=usuario)
		registroA = DatosAcademicosAlumno.objects.filter(cuenta=usuario)
		if len(registroP)==0:
			registro_solicitud = []
			fecha_solicitud = timezone.now()
		else:
			registro_solicitud = SolicitudReinscripcion.objects.filter(datos_personales=registroP[0])
			if len(registro_solicitud)==0:
				fecha_solicitud = timezone.now()
			else:
				fecha_solicitud = registro_solicitud[len(registro_solicitud)-1].fecha
		if (len(registro_solicitud)>0) and fecha_mayor(fecha_solicitud.strftime("%Y-%m-%d %H:%M:%S"),Calendario.objects.get(nombre="Reinscripción").fecha_inicio.strftime("%Y-%m-%d %H:%M:%S")) and control:
			control = False
			return redirect("failure","2")
	if request.method == "GET":
		forms_programa = FormsetProgramaSem()
		return render(request,"reinscripcion.html",{
			'datosP': registroP[0] if len(registroP) == 1 else "X",
			'datosA': registroA[0] if len(registroA) == 1 else "X",
			'profes': User.objects.filter(is_staff=True),
			'formsPrograma': forms_programa
		})
	
	try:
		if request.user.is_staff:
			solicitud = get_object_or_404(SolicitudReinscripcion,pk=request.POST.get('id_solicitud'))
			solicitud.firma_asesor = comprueba_firma(request.POST.get("firma_asesor"))
			solicitud.firma_jefe = comprueba_firma(request.POST.get("firma_jefe"))
			solicitud.save()
			return redirect('success',"0")
		else:
			new_form_datos_p = actualizar_personales(request,registroP,usuario,FormDatosPersonalesAlumnoCorreo)
			new_form_datos_a = actualizar_academicos(request,registroA,usuario)
			
			if (control):
				form_reinscripcion = FormSolicitudReinscripcion(request.POST)
				new_form_reinscripcion = form_reinscripcion.save(commit=False)
				
				new_form_reinscripcion.jefe = User.objects.get(username='Jefe_area')
			else:
				form_reinscripcion = FormSolicitudReinscripcion(request.POST,instance=registro_solicitud[len(registro_solicitud)-1])
				if form_reinscripcion.is_valid():
					for field in form_reinscripcion.cleaned_data:
						setattr(registro_solicitud[len(registro_solicitud)-1],field, form_reinscripcion.cleaned_data[field])
					new_form_reinscripcion = form_reinscripcion.save(commit=False)
					programa_borrar = ReinscripcionPrograma.objects.filter(id_solicitud_reinscripcion=new_form_reinscripcion)
					for programa in programa_borrar:
						programa.delete()
				else:
					print(form_reinscripcion.errors)
			new_form_reinscripcion.datos_personales = new_form_datos_p
			new_form_reinscripcion.datos_academicos = new_form_datos_a
			new_form_reinscripcion.asesor = User.objects.get(id=request.POST.get('nombre_asesor'))
			new_form_reinscripcion.fecha = timezone.now()
			new_form_reinscripcion.save()
			control = True
			forms_programa = FormsetProgramaSem(request.POST)
			if forms_programa.is_valid():
				for form in forms_programa:
					form_programa = form.cleaned_data.get('id_programa_semestral')
					ReinscripcionPrograma.objects.create(
						id_solicitud_reinscripcion = new_form_reinscripcion,
						id_programa_semestral = form_programa
					)
				print("Programa creado")
				global correo
				correo = request.POST["correo_1"]
				enviar_correo(new_form_reinscripcion.id,"Solicitud de Reinscripción")
			else:
				print(forms_programa.errors)
				return redirect('failure',"3")
			return redirect('success',new_form_reinscripcion.id)
	except Exception as error:
		forms_programa = FormsetProgramaSem()
		return render(request,"reinscripcion.html",{
			'datosP': registroP[0] if len(registroP) == 1 else "X",
			'datosA': registroA[0] if len(registroA) == 1 else "X",
			'formReinscipcion': FormSolicitudReinscripcion,	
			'formsPrograma': forms_programa,
			'error': error,
		})

#PROGRAMA INDIVIDUAL DE ACTIVIDADES -----------------------------------------------------------
@login_required
def programa_actividades(request):
	global control
	usuario = request.user
	registroP = DatosPersonalesAlumno.objects.filter(cuenta=usuario)
	registroA = DatosAcademicosAlumno.objects.filter(cuenta=usuario)
	if len(registroP)==0:
		registro_solicitud = []
	else:
		registro_solicitud = ConstanciaProgramaIndividual.objects.filter(datos_personales=registroP[0])
	if (len(registro_solicitud)>0) and control:
		control = False
		return redirect("failure","1")
	if request.method == "GET":
		forms_programa = FormsetProgramaSem()
		return render(request,"programaActividades.html",{
			'datosP': registroP[0] if len(registroP) == 1 else "X",
			'datosA': registroA[0] if len(registroA) == 1 else "X",
			'formCosntacia': FormConstanciaProgramaIndividual,
			'formsPrograma': forms_programa
		})
	try:
		if request.user.is_staff:
			solicitud = get_object_or_404(ConstanciaProgramaIndividual,pk=request.POST.get('id_solicitud'))
			solicitud.firma_asesor = comprueba_firma(request.POST.get("firma_asesor"))
			solicitud.firma_jefe = comprueba_firma(request.POST.get("firma_jefe"))
			solicitud.save()
			return redirect('success',"0")
		else:
			new_form_datos_p = actualizar_personales(request,registroP,usuario)
			new_form_datos_a = actualizar_academicos(request,registroA,usuario)

			form_constancia = FormConstanciaProgramaIndividual(request.POST)
			new_form_constancia = form_constancia.save(commit=False)
			new_form_constancia.datos_personales = new_form_datos_p
			new_form_constancia.datos_academicos = new_form_datos_a
			new_form_constancia.fecha = timezone.now()
			new_form_constancia.save()

			forms_programa = FormsetProgramaSem(request.POST)
			if forms_programa.is_valid():
				for form in forms_programa:
					claveu = form.cleaned_data.get('clave')
					unidad = form.cleaned_data.get("unidad_aprendizaje")
					creditosm = form.cleaned_data.get("creditos")
					periodom = form.cleaned_data.get("periodo")
					lugar = form.cleaned_data.get("lugar_realizacion")

					form_programa = ProgramaSemestral.objects.create(
						clave = claveu,
						unidad_aprendizaje = unidad,
						creditos = creditosm,
						periodo = periodom,
						lugar_realizacion = lugar,
					)
					ConstanciaPrograma.objects.create(
						id_constancia_programa_individual = new_form_constancia,
						id_programa_actividades = form_programa
					)
				global correo
				correo = request.POST["correo_1"]
				enviar_correo(solicitud.id,"Inscripcion al programa individual de Actividades")
			else:
				print(forms_programa.errors)		
			return redirect('success',new_form_constancia.id)
		
	except Exception as error:
		forms_programa = FormsetProgramaSem()
		return render(request,"programaActividades.html",{
			'datosP': registroP[0] if len(registroP) == 1 else "X",
			'datosA': registroA[0] if len(registroA) == 1 else "X",
			'formCosntacia': FormConstanciaProgramaIndividual,
			'formsPrograma': forms_programa,
			'error':error
		})

#ACTA DE REGITRO DE TESIS ---------------------------------------------------------------------
@login_required
def tesis_registro(request):
	global control
	usuario = request.user
	registroP = DatosPersonalesAlumno.objects.filter(cuenta=usuario)
	registroA = DatosAcademicosAlumno.objects.filter(cuenta=usuario)
	if len(registroP)==0:
		registro_solicitud = []
	else:
		registro_solicitud = ConstanciaProgramaIndividual.objects.filter(datos_personales=registroP[0])
	if (len(registro_solicitud)>0) and control:
		control = False
		return redirect("failure","1")
	if request.method == "GET":
		return render(request,"registroTesis.html",{
			'datosP': registroP[0] if len(registroP) == 1 else "X",
			'datosA': registroA[0] if len(registroA) == 1 else "X",
			'formTesis': FormActaRegistroTemaTesis
		})
	
	try:
		if request.user.staff:
			solicitud = get_object_or_404(ActaRegistroTemaTesis,pk=request.POST.get('id_solicitud'))
			form_colegio = FormColegioProfesoresPosgrado(request.POST)
			new_form_colegio = form_colegio.save()
			solicitud.colegio_profesores = new_form_colegio
			solicitud.firma_director_1 = comprueba_firma(request.POST.get("firma_director_1"))
			solicitud.firma_director_2 = comprueba_firma(request.POST.get("firma_director_2"))
			solicitud.firma_presidente_colegio = comprueba_firma(request.POST.get("firma_presidente_colegio"))
			solicitud.save()
			return redirect('success',"0")
		else:
			form_datos_p = FormDatosPersonalesAlumno(request.POST)
			form_datos_a = FormDatosAcademicosAlumnoIns(request.POST)
			form_tesis = FormActaRegistroTemaTesis(request.POST)
			new_form_datos_p = form_datos_p.save()
			new_form_datos_a = form_datos_a.save()
			new_form_tesis = form_tesis.save(commit=False)
			new_form_tesis.datos_personales = new_form_datos_p
			new_form_tesis.datos_academicos = new_form_datos_a
			new_form_tesis.save()
			global correo
			correo = request.POST["correo_1"]
			enviar_correo(solicitud.id,"Acta de registro de tema de tesis")
			return redirect('success',form_tesis.id)
		
	except Exception as error:
		return render(request,"registroTesis.html",{
			'datosP': registroP[0] if len(registroP) == 1 else "X",
			'datosA': registroA[0] if len(registroA) == 1 else "X",
			'formTesis': FormActaRegistroTemaTesis,
			"error": error
		})

#ACTA DE REVISIÓN DE TESIS --------------------------------------------------------------------
@login_required
def tesis_revision(request):
	if request.method == "GET":
		return render(request,"revisionTesis.html",{
#			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoTesis,
			'formColegio': FormColegioProfesoresPosgradoRev,
			'formTesis': FormActaRevisionTemaTesis
		})
	
	try:
		form_datos_p = FormDatosPersonalesAlumno(request.POST)
		form_datos_a = FormDatosAcademicosAlumnoIns(request.POST)
		form_colegio = FormColegioProfesoresPosgrado(request.POST)
		form_tesis = FormActaRevisionTemaTesis(request.POST)
		new_form_datos_p = form_datos_p.save()
		new_form_datos_a = form_datos_a.save()
		new_form_colegio = form_colegio.save()
		new_form_tesis = form_tesis.save(commit=False)
		new_form_tesis.datos_personales = new_form_datos_p
		new_form_tesis.datos_academicos = new_form_datos_a
		new_form_tesis.colegio_profesores = new_form_colegio
		new_form_tesis.save()
		return redirect('success')
	except Exception as error:
		return render(request,"revisionTesis.html",{
#			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoTesis,
			'formColegio': FormColegioProfesoresPosgradoRev,
			'formTesis': FormActaRevisionTemaTesis,
			"error": error
		})

#INICIAR SESIÓN -------------------------------------------------------------------------------
def signin(request):
	if request.method == "GET":
		return render(request, "index.html",{
			'form': AuthenticationForm,
			'usuario': request.user.first_name if request.user.is_authenticated else "Invitado" 
		})
	try:
		username=request.POST['username']
		password=request.POST['password']
		user = User.objects.get(username=username)
		if not user.is_active:
			return render(request, "index.html", { "error": "Tu cuenta está inactiva. Contacta al administrador." })
		auth = authenticate(request,username=username,password=password)
		if auth is None:
			return render(request, "index.html",{
				'form': AuthenticationForm,
				'error': "Credenciales incorrectas. Intenta nuevamente"
			})
		else:
			login(request,auth)
			return redirect("index")
	except User.DoesNotExist:
		return render(request, "index.html", { "error": "Usuario no registrado." })

#CERRAR SESIÓN --------------------------------------------------------------------------------
@login_required
def signout(request):
	logout(request)
	return redirect("index")

@login_required
def success(request,tipo):
	return render(request, "responseHTML/success.html",{"tipo":tipo})

def crear_superusuario(request):
	if not User.objects.filter(username='admin').exists():
		User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='tevill5393941'
        )
		User.objects.create_superuser(
            username='eter',
			first_name='Admin',
			last_name='01',
            email='admin@example.com',
            password='tevill5393941'
        )
		alumno = User.objects.create_user(
			username='alumno',
			password='alu123456',
			first_name='Fabian',
			last_name='Hernandez',
			email='smpmo.p@gmail.com'
		)
		alumno.is_active = True
		alumno.is_staff = False
		alumno.is_superuser = False
		profesor = User.objects.create_user(
			username='profesor',
			password='profe123',
			first_name='Profesor',
			last_name='01',
			email='profe@ipn.mx.com'
		)
		profesor.is_active = True
		profesor.is_staff = True
		profesor.is_superuser = False
		return redirect('success',"0")
	else:
		return redirect('failure',"0")

@login_required
def generar_pdf(request):
	try:
		data_string = request.POST.get("dato")
		data_dict = ast.literal_eval(data_string)
		if data_dict["tipo"] == "Solicitud_Inscripcion":
			data_dict["antecedentes"] = ast.literal_eval(data_dict["antecedentes"])
			data_dict["programa"] = ast.literal_eval(data_dict["programa"])
			return render(request, "pdfs/base_pdf.html", data_dict)
		elif data_dict["tipo"] == "Solicitud_Reinscripcion":
			data_dict["programa"] = ast.literal_eval(data_dict["programa"])
			print(data_dict)
			return redirect("success","0")
	except Exception as error:
		return HttpResponse(f'Error al generar el PDF {error}')

