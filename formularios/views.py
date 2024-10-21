from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
	return render(request, "index.html")

def crear_solicitud_inscripcion(request):
	if request.method == "GET":
		return render(request,"inscripcion.html",{
			'form1': FormDatosPersonalesAlumno,
			'form2': FormDatosAcademicosAlumno,
			'form3': FormAntecedentesAcademicos,
			'form4': FormProgramaSemestral,
			'form5': FormSolicitudInscripcion
		})
	else:
		try:
			form1 = FormDatosPersonalesAlumno(request.POST)
			form2 = FormDatosAcademicosAlumno(request.POST)
			form3 = FormAntecedentesAcademicos(request.POST)
			form4 = FormProgramaSemestral(request.POST)
			form5 = FormSolicitudInscripcion(request.POST)
			new_form1 = form1.save()
			new_form2 = form2.save()
			new_form3 = form3.save()
			new_form4 = form4.save()
			new_form5 = form5.save(commit=False)
			new_form5.datos_personales_id = new_form1.id
			new_form5.datos_academicos_id = new_form2.id
			new_form5.programa_semestral_id = new_form4.id
			new_form5.save()
			form6 = InscripcionAntecedentes.objects.create(
				id_solicitud_inscripcion = new_form5,
				id_antecedentes = new_form3
			)
			form6.save()
			
			return redirect('index')
		except Exception as error:
			return render(request,"inscripcion.html",{
			'form1': FormDatosPersonalesAlumno,
			'form2': FormDatosAcademicosAlumno,
			'form3': FormAntecedentesAcademicos,
			'form4': FormProgramaSemestral,
			'form5': FormSolicitudInscripcion,
			'error': error
		})