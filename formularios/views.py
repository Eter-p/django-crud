from django.shortcuts import render,redirect,get_object_or_404
from .forms import *

form_solicitud = None

# Pantalla de inicio
def index(request):
	return render(request, "index.html")

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
		form_datos_p = FormDatosPersonalesAlumnoIns(request.POST)
		form_datos_a = FormDatosAcademicosAlumnoIns(request.POST)
		new_form_datos_p = form_datos_p.save()
		new_form_datos_a = form_datos_a.save()
		new_form_inscripcion = SolicitudInscripcion.objects.create(
			datos_personales = new_form_datos_p,
			datos_academicos = new_form_datos_a
		)
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
		solicitud = get_object_or_404(SolicitudInscripcion,pk=form_solicitud.id)
		form_inscripcion = FormSolicitudInscripcion(request.POST,instance=solicitud)
		form_inscripcion.save()
		return redirect('index')
	except Exception as error:
		return render(request,"inscripcion/inscripcionFirmas.html",{
			'formF':SolicitudInscripcion,
			'error': error}
		)

# REINSCRIPCION--------------------------------------------------------------------------------
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
		else:
			print(forms_programa.errors)		
		return redirect('index')
	except Exception as error:
		forms_programa = FormsetProgramaSem()
		return render(request,"reinscripcion.html",{
			'error': error,
			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoRei,
			'formReinscipcion': FormSolicitudReinscripcion	,	
			'formsPrograma': forms_programa
		})

#PROGRAMA INDIVIDUAL DE ACTIVIDADES
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
		else:
			print(forms_programa.errors)		
		return redirect('index')
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

#ACTA DE REGITRO DE TESIS
def tesis_registro(request):
	if request.method == "GET":
		return render(request,"registroTesis.html",{
			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoTesis,
			'formColegio': FormColegioProfesoresPosgrado,
			'formTesis': FormActaRegistroTemaTesis
		})
	
	try:
		form_datos_p = FormDatosPersonalesAlumnoIns(request.POST)
		form_datos_a = FormDatosAcademicosAlumnoIns(request.POST)
		form_colegio = FormColegioProfesoresPosgrado(request.POST)
		form_tesis = FormActaRegistroTemaTesis(request.POST)
		new_form_datos_p = form_datos_p.save()
		new_form_datos_a = form_datos_a.save()
		new_form_colegio = form_colegio.save()
		new_form_tesis = form_tesis.save(commit=False)
		new_form_tesis.datos_personales = new_form_datos_p
		new_form_tesis.datos_academicos = new_form_datos_a
		new_form_tesis.colegio_profesores = new_form_colegio
		new_form_tesis.save()
		return redirect('index')
	except Exception as error:
		return render(request,"registroTesis.html",{
			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoTesis,
			'formColegio': FormColegioProfesoresPosgrado,
			'formTesis': FormActaRegistroTemaTesis,
			"error": error
		})

#ACTA DE REVISIÓN DE TESIS
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
		return redirect('index')
	except Exception as error:
		return render(request,"revisionTesis.html",{
			'formDatosP': FormDatosPersonalesAlumnoRei,
			'formDatosA': FormDatosAcademicosAlumnoTesis,
			'formColegio': FormColegioProfesoresPosgradoRev,
			'formTesis': FormActaRevisionTemaTesis,
			"error": error
		})
