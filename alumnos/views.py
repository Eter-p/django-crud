from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .forms import FormDatosPersonales,FormDatosAcademicos
from .models import DatosPersonalesAlumno,DatosAcademicosAlumno
from .utils import actualizar_datos

#Registro y actualizacion de datos personales
@login_required
def registro_datos_p(request):
	usuario = request.user
	registro = DatosPersonalesAlumno.objects.filter(cuenta=usuario)
	if request.method == "GET":
		return render(request,"actualizacion/DatosPersonales.html",{
			'datosP': registro[0] if len(registro) == 1 else "X"
		})
	try:
		actualizar_datos(request,registro,usuario,FormDatosPersonales)
		return redirect('success',"actualizacion")
	except Exception as error:
		return render(request,"actualizacion/DatosPersonales.html",{
			'datosP': registro[0] if len(registro) == 1 else "X",
			'error': error 
		})

#Registro y actualizacion de datos academicos
@login_required
def registro_datos_a(request):
	usuario = request.user
	registro = DatosAcademicosAlumno.objects.filter(cuenta=usuario)
	if request.method == "GET":
		return render(request,"actualizacion/DatosAcademicos.html",{
			'datosA': registro[0] if len(registro) == 1 else "X"
		})
	try:
		actualizar_datos(request,registro,usuario,FormDatosAcademicos)
		return redirect('success',"actualizacion")
	except Exception as error:
		return render(request,"actualizacion/DatosAcademicos.html",{
			'datosA': registro[0] if len(registro) == 1 else "X",
			'error': error 
		})
