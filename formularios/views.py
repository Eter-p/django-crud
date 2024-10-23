from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
	return render(request, "index.html")

def crear_solicitud_inscripcion(request):
	if request.method == "GET":
		forms3 = FormsetAntecedentes()
		forms4 = FormsetProgramaIns()
		return render(request,"inscripcion.html",{
			'form1': FormDatosPersonalesAlumno,
			'form2': FormDatosAcademicosAlumno,
			'forms3': forms3,
			'form4': FormProgramaSemestral,
			'form5': FormSolicitudInscripcion
		})
	else:
		try:
			form1 = FormDatosPersonalesAlumno(request.POST)
			form2 = FormDatosAcademicosAlumno(request.POST)
			forms3 = FormsetAntecedentes(request.POST)
			form4 = FormsetProgramaIns(request.POST)
			form5 = FormSolicitudInscripcion(request.POST)
			new_form1 = form1.save()
			new_form2 = form2.save()
			new_form4 = form4.save()	
			new_form5 = form5.save(commit=False)
			new_form5.datos_personales_id = new_form1.id
			new_form5.datos_academicos_id = new_form2.id
			new_form5.programa_semestral_id = new_form4.id
			new_form5.save()
			print(forms3)
			if forms3.is_valid():
				for form in forms3:
					nivel = form.cleaned_data.get('nivel_academico_cursado')
					programa = form.cleaned_data.get("programa_academico_cursado")
					institucion = form.cleaned_data.get("institucion_donde_curso")
					estado = form.cleaned_data.get("estado_institucion")
					fecha = form.cleaned_data.get("fecha_graduacion")
					form3 = AntecedentesAcademicos.objects.create(
						nivel_academico_cursado = nivel,
						programa_academico_cursado = programa,
						institucion_donde_curso = institucion,
						estado_institucion = estado,
						fecha_graduacion = fecha
					)
#					new_form3 = form3.save()
					new_form6 = InscripcionAntecedentes.objects.create(
						id_solicitud_inscripcion = new_form5,
						id_antecedentes = form3
					)
					new_form6.save()
			else:
				print(forms3.errors)
			return redirect('index')
		except Exception as error:
			forms3 = FormsetAntecedentes()
			forms4 = FormsetProgramaIns()
			return render(request,"inscripcion.html",{
			'form1': FormDatosPersonalesAlumno,
			'form2': FormDatosAcademicosAlumno,
			'forms3': forms3,
			'forms4': forms4,
			'form5': FormSolicitudInscripcion,
			'error': error 
		})