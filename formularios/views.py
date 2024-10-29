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
# INSCRIPCIÓN
def solicitud_inscripcion_1(request):
	if request.method == "GET":
		return render(request,"inscripcion/inscripcion1.html",{
			'form1': FormDatosPersonalesAlumno,
			'form2': FormDatosAcademicosAlumno,
		})
	
	try:
		global form_solicitud
		form1 = FormDatosPersonalesAlumno(request.POST)
		form2 = FormDatosAcademicosAlumno(request.POST)
		new_form1 = form1.save()
		new_form2 = form2.save()
		new_form3 = SolicitudInscripcion.objects.create(
			datos_personales = new_form1,
			datos_academicos = new_form2
		)
		form_solicitud = new_form3
		return redirect('solicitud_inscripcion_2')
	except Exception as error:
		return render(request,"inscripcion/inscripcion1.html",{
		'form1': FormDatosPersonalesAlumno,
		'form2': FormDatosAcademicosAlumno,
		'form3': FormSolicitudInscripcion,
		'error': error 
	})

def solicitud_inscripcion_2(request):
	if request.method == "GET":
		formsA = FormsetAntecedentes()
		return render(request,"inscripcion/inscripcion2.html",{'formsA': formsA})
	try:
		formsA = FormsetAntecedentes(request.POST)
		if formsA.is_valid():
			for form in formsA:
				nivel = form.cleaned_data.get('nivel_academico_cursado')
				programa = form.cleaned_data.get("programa_academico_cursado")
				institucion = form.cleaned_data.get("institucion_donde_curso")
				estado = form.cleaned_data.get("estado_institucion")
				fecha = form.cleaned_data.get("fecha_graduacion")
				form = AntecedentesAcademicos.objects.create(
					nivel_academico_cursado = nivel,
					programa_academico_cursado = programa,
					institucion_donde_curso = institucion,
					estado_institucion = estado,
					fecha_graduacion = fecha
				)
				new_form = InscripcionAntecedentes.objects.create(
					id_solicitud_inscripcion = form_solicitud,
					id_antecedentes = form
				)
				new_form.save()
		else:
			print(formsA.errors)
		return redirect('solicitud_inscripcion_3')
	except Exception as error:
		formsA = FormsetAntecedentes()
		return render(request,"inscripcion.html",{
			'formsA': formsA,
			'error': error 
		})

def solicitud_inscripcion_3(request):
	if request.method == "GET":
		formsP = FormsetProgramaIns()
		return render(request,"inscripcion/inscripcion3.html",{'formsP': formsP})
	try:
		formsP = FormsetProgramaIns(request.POST)
		if formsP.is_valid():
			for form in formsP:
				claveu = form.cleaned_data.get('clave')
				unidad = form.cleaned_data.get("unidad_aprendizaje")
				profesorm = form.cleaned_data.get("profesor")
				lugar = form.cleaned_data.get("lugar_realizacion")
				form = ProgramaSemestral.objects.create(
					clave = claveu,
					unidad_aprendizaje = unidad,
					profesor = profesorm,
					lugar_realizacion = lugar,
				)
				new_form = InscripcionPrograma.objects.create(
					id_solicitud_inscripcion = form_solicitud,
					id_programa_semestral = form
				)
				new_form.save()
		else:
			print(formsP.errors)
		return redirect('solicitud_inscripcion_4')
	except Exception as error:
		formsP = FormsetProgramaIns()
		return render(request,"inscripcion.html",{
			'formsP': formsP,
			'error': error 
		})
	
def solicitud_inscripcion_4(request):
	if request.method == 'GET':
		return render(request,"inscripcion/inscripcion4.html",{'form':FormSolicitudInscripcion})
	try:
		solicitud = get_object_or_404(SolicitudInscripcion,pk=form_solicitud.id)
		form = FormSolicitudInscripcion(request.POST,instance=solicitud)
		form.save()
		return redirect('index')
	except Exception as error:
		return render(request,"inscripcion/inscripcion4.html",{
			'form':SolicitudInscripcion,
			'error': error}
		)

