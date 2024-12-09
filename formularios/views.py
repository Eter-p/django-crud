from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404

import datetime as d
import ast

form_solicitud = None
correo = ""

def comprueba_firma(dato):
	if dato == None:
		return False
	else:
		return "on" in dato

# Pantalla de inicio
def index(request):
	return render(request,"index.html")

def formularios(request):
	calendario_inscripcion = Calendario.objects.get(nombre="Inscripción")
	calendario_reinscripcion = Calendario.objects.get(nombre="Reinscripción")
	calendario_programa = Calendario.objects.get(nombre="Programa de Actividades")
	calendario_registro = Calendario.objects.get(nombre="Tesis Registro")
	calendario_revision = Calendario.objects.get(nombre="Tesis Revision")
	return render(request, "formularios.html",{
		"inscripcion":calendario_inscripcion,
		"reinscripcion":calendario_reinscripcion,
		"programa":calendario_programa,
		"registro":calendario_registro,
		"revision":calendario_revision,
	})

#Cancelar solicitud
def solicitud_cancelar(request):
	if request.method == "POST":
		if form_solicitud != None:
			form_solicitud.delete()
		else:
			print("NO hay solicitud")
	else:
		print("GET :X")
	return redirect("index")

# INSCRIPCIÓN --------------------------------------------------------------------------------
def inscripcion_datos(request):
	if request.method == "GET":
		return render(request,"inscripcion/inscripcionDatos.html",{
			'formDatosP': FormDatosPersonalesAlumnoIns,
			'formDatosA': FormDatosAcademicosAlumnoIns,
		})
	
	try:
		global form_solicitud
		global correo
		form_datos_p = FormDatosPersonalesAlumnoIns(request.POST)
		form_datos_a = FormDatosAcademicosAlumnoIns(request.POST)
		new_form_datos_p = form_datos_p.save()
		new_form_datos_a = form_datos_a.save()
		new_form_inscripcion = SolicitudInscripcion.objects.create(
			datos_personales = new_form_datos_p,
			datos_academicos = new_form_datos_a
		)
		correo = request.POST["correo_1"]
		form_solicitud = new_form_inscripcion
		return redirect('inscripcion_antecedentes')
	except Exception as error:
		return render(request,"inscripcion/inscripcionDatos.html",{
			'formDatosP': FormDatosPersonalesAlumnoIns,
			'formDatosA': FormDatosAcademicosAlumnoIns,
			'error': error 
		})

def inscripcion_antecedentes(request):
	if request.method == "GET":
		forms_antecedentes = FormsetAntecedentes()
		return render(request,"inscripcion/inscripcionAntecedentes.html",{'formsA': forms_antecedentes})
	try:
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
		else:
			print(forms_antecedentes)
			print(forms_antecedentes.errors)
		return redirect('inscripcion_programa')
	except Exception as error:
		forms_antecedentes = FormsetAntecedentes()
		return render(request,"inscripcionAntecedentes.html",{
			'formsA': forms_antecedentes,
			'error': error 
		})

def inscripcion_programa(request):
	if request.method == "GET":
		forms_programa = FormsetProgramaSem()
		return render(request,"inscripcion/inscripcionPrograma.html",{'formsP': forms_programa})
	try:
		forms_programa = FormsetProgramaSem(request.POST)
		if forms_programa.is_valid():
			for form in forms_programa:
				claveu = form.cleaned_data.get('clave')
				unidad = form.cleaned_data.get("unidad_aprendizaje")
				profesorm = form.cleaned_data.get("profesor")
				lugar = form.cleaned_data.get("lugar_realizacion")
				form_programa = ProgramaSemestral.objects.create(
					clave = claveu,
					unidad_aprendizaje = unidad,
					profesor = profesorm,
					lugar_realizacion = lugar,
				)
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
	
def inscripcion_firmas(request):
	if request.method == 'GET':
		return render(request,"inscripcion/inscripcionFirmas.html",{'formF':FormSolicitudInscripcion})
	try:
		if request.user.is_authenticated:
			solicitud = get_object_or_404(SolicitudInscripcion,pk=request.POST.get('id_solicitud'))
			firma_asesor = comprueba_firma(request.POST.get("firma_asesor"))
			solicitud.firma_asesor = firma_asesor
			if firma_asesor: solicitud.asesor = request.user.username
			firma_jefe = comprueba_firma(request.POST.get("firma_jefe"))
			solicitud.firma_jefe = firma_jefe
			if firma_jefe: solicitud.jefe = request.user.username
			solicitud.save()
			return redirect('success',"0")
		else:
			solicitud.fecha = request.POST.get("Fecha")
			solicitud = get_object_or_404(SolicitudInscripcion,pk=form_solicitud.id)
			solicitud.firma_alumno = comprueba_firma(request.POST.get("firma_alumno"))
			solicitud.aviso_privacidad = comprueba_firma(request.POST.get("aviso_privacidad"))
			solicitud.save()
			enviar_correo(solicitud.id,"Solicitud de Inscripción")
			return redirect('success',solicitud.id)
	except Exception as error:
		return render(request,"inscripcion/inscripcionFirmas.html",{
			'formF':SolicitudInscripcion,
			'error': error}
		)

# REINSCRIPCION -------------------------------------------------------------------------------
def reinscripcion(request):
	if request.method == "GET":
		forms_programa = FormsetProgramaSem()
		return render(request,"reinscripcion.html",{
			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoRei,
			'formReinscipcion': FormSolicitudReinscripcion	,	
			'formsPrograma': forms_programa
		})
	
	try:
		if request.user.is_authenticated:
			solicitud = get_object_or_404(SolicitudReinscripcion,pk=request.POST.get('id_solicitud'))
			solicitud.firma_asesor = comprueba_firma(request.POST.get("firma_asesor"))
			solicitud.firma_jefe = comprueba_firma(request.POST.get("firma_jefe"))
			solicitud.save()
			return redirect('success',"0")
		else:
			form_datos_p = FormDatosPersonalesAlumnoRei(request.POST)
			form_datos_a = FormDatosAcademicosAlumnoRei(request.POST)
			form_reinscripcicon = FormSolicitudReinscripcion(request.POST)
			forms_programa = FormsetProgramaSem(request.POST)

			new_form_datos_p = form_datos_p.save()
			new_form_datos_a = form_datos_a.save()
			new_form_reinscripcicon = form_reinscripcicon.save(commit=False)
			new_form_reinscripcicon.datos_personales = new_form_datos_p
			new_form_reinscripcicon.datos_academicos = new_form_datos_a
			new_form_reinscripcicon.save()

			if forms_programa.is_valid():
				for form in forms_programa:
					claveu = form.cleaned_data.get('clave')
					unidad = form.cleaned_data.get("unidad_aprendizaje")
					profesorm = form.cleaned_data.get("profesor")
					lugar = form.cleaned_data.get("lugar_realizacion")
					form_programa = ProgramaSemestral.objects.create(
						clave = claveu,
						unidad_aprendizaje = unidad,
						profesor = profesorm,
						lugar_realizacion = lugar,
					)
					ReinscripcionPrograma.objects.create(
						id_solicitud_reinscripcion = new_form_reinscripcicon,
						id_programa_semestral = form_programa
					)
				global correo
				correo = request.POST["correo_1"]
				enviar_correo(new_form_reinscripcicon.id,"Solicitud de Reinscripción")

			else:
				print(forms_programa.errors)	
			return redirect('success',new_form_reinscripcicon.id)
	except Exception as error:
		forms_programa = FormsetProgramaSem()
		return render(request,"reinscripcion.html",{
			'error': error,
			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoRei,
			'formReinscipcion': FormSolicitudReinscripcion	,	
			'formsPrograma': forms_programa
		})

#PROGRAMA INDIVIDUAL DE ACTIVIDADES -----------------------------------------------------------
def programa_actividades(request):
	if request.method == "GET":
		forms_programa = FormsetProgramaInd()
		return render(request,"programaActividades.html",{
			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoRei,
			'formAsesor': FormDatosAsesor,
			'formCosntacia': FormConstanciaProgramaIndividual,
			'formsPrograma': forms_programa
		})
	try:
		if request.user.is_authenticated:
			solicitud = get_object_or_404(ConstanciaProgramaIndividual,pk=request.POST.get('id_solicitud'))
			solicitud.firma_asesor = comprueba_firma(request.POST.get("firma_asesor"))
			solicitud.firma_jefe = comprueba_firma(request.POST.get("firma_jefe"))
			solicitud.save()
			return redirect('success',"0")
		else:
			form_datos_p = FormDatosPersonalesAlumnoRei(request.POST)
			form_datos_a = FormDatosAcademicosAlumnoRei(request.POST)
			form_asesor = FormDatosAsesor(request.POST)
			form_constancia = FormConstanciaProgramaIndividual(request.POST)
			forms_programa = FormsetProgramaInd(request.POST)

			new_form_datos_p = form_datos_p.save()
			new_form_datos_a = form_datos_a.save()
			new_form_asesor = form_asesor.save()
			new_form_constancia = form_constancia.save(commit=False)
			new_form_constancia.datos_personales = new_form_datos_p
			new_form_constancia.datos_academicos = new_form_datos_a
			new_form_constancia.asesor = new_form_asesor
			new_form_constancia.save()

			if forms_programa.is_valid():
				for form in forms_programa:
					claveu = form.cleaned_data.get('clave')
					unidad = form.cleaned_data.get("unidad_aprendizaje")
					creditosm = form.cleaned_data.get("creditos")
					periodom = form.cleaned_data.get("periodo")
					lugar = form.cleaned_data.get("lugar_realizacion")

					form_programa = ProgramaActividades.objects.create(
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
			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoRei,
			'formAsesor': FormDatosAsesor,
			'formCosntacia': FormConstanciaProgramaIndividual,
			'formsPrograma': forms_programa,
			'error':error
		})

#ACTA DE REGITRO DE TESIS ---------------------------------------------------------------------
def tesis_registro(request):
	if request.method == "GET":
		return render(request,"registroTesis.html",{
			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoTesis,
			'formColegio': FormColegioProfesoresPosgrado,
			'formTesis': FormActaRegistroTemaTesis
		})
	
	try:
		if request.user.is_authenticated:
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
			form_datos_p = FormDatosPersonalesAlumnoIns(request.POST)
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
			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoTesis,
			'formColegio': FormColegioProfesoresPosgrado,
			'formTesis': FormActaRegistroTemaTesis,
			"error": error
		})

#ACTA DE REVISIÓN DE TESIS --------------------------------------------------------------------
def tesis_revision(request):
	if request.method == "GET":
		return render(request,"revisionTesis.html",{
			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoTesis,
			'formColegio': FormColegioProfesoresPosgradoRev,
			'formTesis': FormActaRevisionTemaTesis
		})
	
	try:
		form_datos_p = FormDatosPersonalesAlumnoIns(request.POST)
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
			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoTesis,
			'formColegio': FormColegioProfesoresPosgradoRev,
			'formTesis': FormActaRevisionTemaTesis,
			"error": error
		})

#REGISTRO DE USUARIO --------------------------------------------------------------------------
def signup(request):
	if request.method == "GET":
		return render(request,"signup.html")
	if request.POST["password1"] == request.POST["password2"]:
		try:
			user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
			user.is_active = False
			user.save()
			return redirect("success","0")
		except Exception as error:
			return render(request,"signup.html", {
				"error": error
			})

#INICIAR SESIÓN -------------------------------------------------------------------------------
def signin(request):
	if request.method == "GET":
		return render(request, "signin.html",{
			'form': AuthenticationForm
		})
	try:
		username=request.POST['username']
		password=request.POST['password']
		user = User.objects.get(username=username)
		if not user.is_active:
			return render(request, "signin.html", { "error": "Tu cuenta está inactiva. Contacta al administrador." })
		user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
		if user is None:
			return render(request, "signin.html",{
				'form': AuthenticationForm,
				'error': "Credenciales incorrectas. Intenta nuevamente"
			})
		else:
			login(request,user)
			return redirect('index')
	except User.DoesNotExist:
		return render(request, "signin.html", { "error": "Usuario no registrado." })

#CERRAR SESIÓN --------------------------------------------------------------------------------
@login_required
def signout(request):
	logout(request)
	return redirect("index")

def success(request,folio):
	return render(request, "success.html",{"folio":folio})

def enviar_correo(id,tipo):
    asunto = tipo
    mensaje = "Guarda este numero y entregalo a los profesores correspondientes: "+str(id)
    destinatario = correo
    send_mail(
		asunto,
		mensaje,
		'hernandez.hernandez.fabian@gmail.com',  # Desde este correo
		[destinatario],  # A este correo
		fail_silently=False,
	)

def creacion_calendario(request):
	fechas = Calendario.objects.all()
	nombres = ["Inscripción","Reinscripción","Programa de Actividades","Tesis Registro","Tesis Revision"]
	if len(fechas) == 0:
		for nom in nombres:
			Calendario.objects.create(
				nombre = nom,
				fecha_inicio =d.datetime.now(),
				fecha_final = d.datetime.now()+d.timedelta(days=30)
			)
		return HttpResponse("Calendarios creados")
	else:
		return HttpResponse("Los calendarios ya fueron creados")

def crear_superusuario(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='tevill5393941'
        )
        return HttpResponse("Superusuario creado exitosamente.")
    else:
        return HttpResponse("El superusuario ya existe.")

@login_required
def generar_pdf(request):
	try:
		data_string = request.POST.get("dato")
		data_dict = ast.literal_eval(data_string)
		data_dict["antecedentes"] = ast.literal_eval(data_dict["antecedentes"])
		data_dict["programa"] = ast.literal_eval(data_dict["programa"])
		return render(request, "pdfs/base_pdf.html", data_dict)
	except Exception as error:
		return HttpResponse(f'Error al generar el PDF{error}')
