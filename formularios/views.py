from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404

from alumnos.models import DatosPersonalesAlumno,DatosAcademicosAlumno
from alumnos.forms import FormDatosPersonales,FormDatosAcademicos,FormDatosAcademicosIns,FormDatosPersonalesCorreo
from alumnos.utils import actualizar_datos
from .models import InscripcionAntecedentes,SolicitudInscripcion,AntecedentesAcademicos,SolicitudReinscripcion,ConstanciaProgramaIndividual
from .forms import FormsetAntecedentes,FormSolicitudInscripcion,FormSolicitudReinscripcion,FormConstanciaProgramaIndividual
from .utils import control,form_solicitud,informacion_inscripcion,enviar_correo,es_antiguo,comprueba_firma,informacion_reinscripcion
from programa.forms import FormsetProgramaSem
from programa.models import InscripcionPrograma,ReinscripcionPrograma,ConstanciaPrograma,ProgramaSemestral
from calendarios.models import Calendario
from tesis.forms import *
import ast

# INSCRIPCIÓN --------------------------------------------------------------------------------
def solicitud_cancelar(request):
	if request.method == "POST":
		if form_solicitud != None:
			form_solicitud.delete()
		else:
			print("NO hay solicitud")
	return redirect("index")

@login_required
def inscripcion_datos(request):
	global control
	usuario = request.user
	registroP = DatosPersonalesAlumno.objects.filter(cuenta=usuario)
	registroA = DatosAcademicosAlumno.objects.filter(cuenta=usuario)
	if len(registroP)==0:
		registro_solicitud = []
		fecha_solicitud = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
	else:
		registro_solicitud = SolicitudInscripcion.objects.filter(datos_personales=registroP[0])
		if len(registro_solicitud)==0:
			fecha_solicitud = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
		else:
			fecha_solicitud = registro_solicitud[0].fecha.strftime("%Y-%m-%d %H:%M:%S")
	antiguo = es_antiguo(fecha_solicitud,Calendario.objects.get(nombre="Inscripción").fecha_inicio.strftime("%Y-%m-%d %H:%M:%S"))	
	if (len(registro_solicitud)!=0) and control:
		control = False
		return render(request,"responseHTML/failure.html",{"tipo":"inscripcion","es_antiguo":antiguo})
	
	if request.method == "GET":
		return render(request,"inscripcion/inscripcionDatos.html",{
			'datosP': registroP[0] if len(registroP) == 1 else "X",
			'datosA': registroA[0] if len(registroA) == 1 else "X",
		})
	try:
		global form_solicitud
		new_form_datos_p = actualizar_datos(request,registroP,usuario,FormDatosPersonales)
		new_form_datos_a = actualizar_datos(request,registroA,usuario,FormDatosAcademicosIns)
		
		if (len(registro_solicitud)==0):
			new_form_inscripcion = SolicitudInscripcion.objects.create(
				datos_personales = new_form_datos_p,
				datos_academicos = new_form_datos_a,
				fecha = timezone.now()
			)
			form_solicitud = new_form_inscripcion
		else:
			form_solicitud = registro_solicitud[0]
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
	print(form_solicitud)
	print(form_solicitud.datos_personales)
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
		return redirect("failure","invalid")
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
			return redirect('inscripcion_firmas')
		return("failure","invalid")
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
	if request.method == 'GET':
		if usuario.is_staff:
			datos = informacion_inscripcion(form_solicitud)
			datos["antecedentes"] = ast.literal_eval(datos["antecedentes"])
			datos["programa"] = ast.literal_eval(datos["programa"])
			return render(request,"firmado/inscripcionFirmas.html",{
				'usuario':usuario,
				'datos': datos,
			})
		get_object_or_404(SolicitudInscripcion,pk=form_solicitud.id)
		return render(request,"firmado/inscripcionFirmas.html",{
			'profes': User.objects.filter(is_staff=True),
		})
	try:
		if usuario.is_staff:
			solicitud = get_object_or_404(SolicitudInscripcion,pk=form_solicitud.id)
			usuario_docente = usuario.username
			if usuario_docente == "Jefe_area":
				solicitud.firma_jefe = True
			if usuario_docente == solicitud.asesor.username:
				solicitud.firma_asesor = True
			solicitud.save()
			form_solicitud = None
			return render(request,'responseHTML/success.html',{"tipo":"firmaInscripcion"})
		form_inscripcion = FormSolicitudInscripcion(request.POST,instance=form_solicitud)
		new_form_inscripcion = form_inscripcion.save()
		new_form_inscripcion.jefe = User.objects.get(username='Jefe_area')
		new_form_inscripcion.save()
		new_form_inscripcion.firma_alumno = comprueba_firma(request.POST.get("firma_alumno"))	
		new_form_inscripcion.aviso_privacidad = comprueba_firma(request.POST.get("aviso_privacidad"))	
		form_solicitud = None
		enviar_correo(new_form_inscripcion.id,"Solicitud de Inscripción",usuario.email)
		return render(request,'responseHTML/success.html',{"tipo":"inscripcion"})
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
		return render(request,"responseHTML/failure.html",{"tipo":"firmas"})

# REINSCRIPCION -------------------------------------------------------------------------------
@login_required
def reinscripcion(request):
	global control
	global form_solicitud
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
		if (len(registro_solicitud)>0) and not es_antiguo(fecha_solicitud.strftime("%Y-%m-%d %H:%M:%S"),Calendario.objects.get(nombre="Reinscripción").fecha_inicio.strftime("%Y-%m-%d %H:%M:%S")) and control:
			control = False
			return render(request,"responseHTML/failure.html",{"tipo":"reinscripcion"})
	if request.method == "GET":
		if usuario.is_staff:
			datos = informacion_reinscripcion(form_solicitud)
			datos["programa"] = ast.literal_eval(datos["programa"])
			return render(request,"reinscripcion.html",{
				'usuario':usuario,
				'datos': datos,
			})
		forms_programa = FormsetProgramaSem()
		return render(request,"reinscripcion.html",{
			'datosP': registroP[0] if len(registroP) == 1 else "X",
			'datosA': registroA[0] if len(registroA) == 1 else "X",
			'profes': User.objects.filter(is_staff=True),
			'formsPrograma': forms_programa
		})
	
	try:
		if usuario.is_staff:
			usuario_docente = usuario.username
			solicitud = get_object_or_404(SolicitudReinscripcion,pk=form_solicitud.id)
			if usuario_docente == "Jefe_area":
				solicitud.firma_jefe = True
			if usuario_docente == solicitud.asesor.username:
				solicitud.firma_asesor = True
			solicitud.save()
			form_solicitud = None
			return render(request,"responseHTML/success.html",{"tipo":"firmaReinscripcion"})

		new_form_datos_p = actualizar_datos(request,registroP,usuario,FormDatosPersonalesCorreo)
		new_form_datos_a = actualizar_datos(request,registroA,usuario,FormDatosAcademicos)
		if (control):
			form_reinscripcion = FormSolicitudReinscripcion(request.POST)
			if not form_reinscripcion.is_valid():
				return render(request,"responseHTML/failure.html",{"tipo":"invalid"})
			new_form_reinscripcion = form_reinscripcion.save(commit=False)
			new_form_reinscripcion.datos_personales = new_form_datos_p
			new_form_reinscripcion.datos_academicos = new_form_datos_a
		else:
			form_reinscripcion = FormSolicitudReinscripcion(request.POST,instance=registro_solicitud[len(registro_solicitud)-1])
			if not form_reinscripcion.is_valid():
				print(form_reinscripcion.errors)
				return render(request,"responseHTML/failure.html",{"tipo":"invalid"})
			new_form_reinscripcion = form_reinscripcion.save(commit=False)
			programa_borrar = ReinscripcionPrograma.objects.filter(id_solicitud_reinscripcion=new_form_reinscripcion)
			for programa in programa_borrar:
				programa.delete()
		new_form_reinscripcion.firma_alumno = comprueba_firma(request.POST.get("firma_alumno"))	
		new_form_reinscripcion.requiere_unidad = comprueba_firma(request.POST.get("requiere_unidad"))	
		new_form_reinscripcion.jefe = User.objects.get(username='Jefe_area')
		new_form_reinscripcion.fecha = timezone.now()
		new_form_reinscripcion.save()
		control = True

		forms_programa = FormsetProgramaSem(request.POST)
		if not forms_programa.is_valid():
			return render(request,"responseHTML/failure.html",{"tipo":"invalid"})
		for form in forms_programa:
			form_programa = form.cleaned_data.get('id_programa_semestral')
			ReinscripcionPrograma.objects.create(
				id_solicitud_reinscripcion = new_form_reinscripcion,
				id_programa_semestral = form_programa
			)
		enviar_correo(new_form_reinscripcion.id,"Solicitud de Reinscripción",new_form_datos_p.cuenta.email)
		return render(request,"responseHTML/success.html",{"tipo":"reinscripcion"})
	except Exception as error:
		forms_programa = FormsetProgramaSem()
		return render(request,"reinscripcion.html",{
			'datosP': registroP[0] if len(registroP) == 1 else "X",
			'datosA': registroA[0] if len(registroA) == 1 else "X",
			'formReinscipcion': FormSolicitudReinscripcion,	
			'formsPrograma': forms_programa,
			'error': error,
		})

def reinscripcion_firmas_pendiente(request):
	if request.method == 'GET':
		usuario = request.user
		if usuario.username == "Jefe_area":
			solicitudes_usuario = SolicitudReinscripcion.objects.all()
			pendientes = solicitudes_usuario.filter(firma_jefe = False)|solicitudes_usuario.filter(firma_jefe = None)
			no_pendientes = SolicitudReinscripcion.objects.all().filter(firma_jefe = True)
		else:
			solicitudes_usuario = SolicitudReinscripcion.objects.filter(asesor=usuario)
			pendientes = solicitudes_usuario.filter(firma_asesor = False)|solicitudes_usuario.filter(firma_asesor = None)
			no_pendientes = SolicitudReinscripcion.objects.filter(asesor=usuario).filter(firma_asesor = True)
		return render(request,"firmado/reinscripcionFirmasStaff.html",{
			'solicitudesP':pendientes,
			'solicitudesN':no_pendientes,
		})
	try:
		global form_solicitud
		form_solicitud = SolicitudReinscripcion.objects.get(id=request.POST.get("solicitud_id"))
		return redirect("reinscripcion")
	except:
		return render(request,"responseHTML/failure.html",{"tipo":"firma"})

# #PROGRAMA INDIVIDUAL DE ACTIVIDADES -----------------------------------------------------------
@login_required
def programa_actividades(request):
	global control
	global form_solicitud
	usuario = request.user
	registroP = DatosPersonalesAlumno.objects.filter(cuenta=usuario)
	registroA = DatosAcademicosAlumno.objects.filter(cuenta=usuario)
	if len(registroP)==0:
		registro_solicitud = []
	else:
		registro_solicitud = ConstanciaProgramaIndividual.objects.filter(datos_personales=registroP[0])
	if (len(registro_solicitud)>0) and control:
		control = False
		return redirect("failure","programa")
	if request.method == "GET":
		if usuario.is_staff:
			datos = informacion_reinscripcion(form_solicitud)
			datos["programa"] = ast.literal_eval(datos["programa"])
			return render(request,"reinscripcion.html",{
				'usuario':usuario,
				'datos': datos,
			})
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
			new_form_datos_p = actualizar_datos(request,registroP,usuario)
			new_form_datos_a = actualizar_datos(request,registroA,usuario)

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

# #ACTA DE REGITRO DE TESIS ---------------------------------------------------------------------
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
			form_datos_p = FormDatosPersonales(request.POST)
			form_datos_a = FormDatosAcademicosIns(request.POST)
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

# #ACTA DE REVISIÓN DE TESIS --------------------------------------------------------------------
@login_required
def tesis_revision(request):
	if request.method == "GET":
		return render(request,"revisionTesis.html",{
#			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicos,
			'formColegio': FormColegioProfesoresPosgradoRev,
			'formTesis': FormActaRevisionTemaTesis
		})
	
	try:
		form_datos_p = FormDatosPersonales(request.POST)
		form_datos_a = FormDatosAcademicos(request.POST)
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
			'formDatosA': FormDatosAcademicos,
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
def success(request):
	return render(request, "responseHTML/success.html")

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
		data_dict["programa"] = ast.literal_eval(data_dict["programa"])
		if data_dict["tipo"] == "Solicitud_Inscripcion":
			data_dict["antecedentes"] = ast.literal_eval(data_dict["antecedentes"])
			return render(request, "pdfs/inscripcion_pdf.html", data_dict)
		if data_dict["tipo"] == "Solicitud_Reinscripcion":
			return render(request, "pdfs/reinscripcion_pdf.html", data_dict)
	except Exception as error:
		return HttpResponse(f'Error al generar el PDF {error}')

