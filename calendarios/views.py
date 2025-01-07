from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils import timezone

import datetime as d

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
		return redirect("success","0")
	else:
		return redirect("failure","0")

@login_required
def info_formularios(request):
	calendario_inscripcion = Calendario.objects.get(nombre="Inscripción")
	calendario_reinscripcion = Calendario.objects.get(nombre="Reinscripción")
	calendario_programa = Calendario.objects.get(nombre="Programa de Actividades")
	calendario_registro = Calendario.objects.get(nombre="Tesis Registro")
	calendario_revision = Calendario.objects.get(nombre="Tesis Revision")
	
	now = timezone.now()
	calendario_inscripcion.activo = calendario_inscripcion.fecha_inicio <= now <= calendario_inscripcion.fecha_final
	calendario_reinscripcion.activo = calendario_reinscripcion.fecha_inicio <= now <= calendario_reinscripcion.fecha_final
	calendario_programa.activo = calendario_programa.fecha_inicio <= now <= calendario_programa.fecha_final
	calendario_registro.activo = calendario_registro.fecha_inicio <= now <= calendario_registro.fecha_final
	calendario_revision.activo = calendario_revision.fecha_inicio <= now <= calendario_revision.fecha_final
	return render(request, "formularios.html",{
		"inscripcion":calendario_inscripcion,
		"reinscripcion":calendario_reinscripcion,
		"programa":calendario_programa,
		"registro":calendario_registro,
		"revision":calendario_revision
	})

