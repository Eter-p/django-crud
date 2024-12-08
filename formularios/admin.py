from django.contrib import admin
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render

from .models import *

admin.site.site_title = "SEPI - Administración"
admin.site.site_header = "Panel de Administración"
admin.site.index_title = "Bienvenido al Administrador"

def generar_pdf(modeladmin,request, queryset):
        try:
            datos = []
            for obj in queryset:
                datos.append({ 'nombre': f'PDF para {obj.datos_personales.nombre}', 'abrir_en_nueva_pestana': True,})
            return render(request,"pdfs/lanzador.html",{
                'datos': datos,
            })
        except Exception as error:
            return HttpResponse('Error al generar el PDF')

class SolicitudInscripcionAdmin(admin.ModelAdmin):
    list_display = ('datos_personales', 'datos_academicos','firma_asesor','firma_jefe')  # Campos que se mostrarán en la lista
    search_fields = ('datos_personales__nombre','datos_personales__apellido_paterno','datos_personales__apellido_materno', 'datos_academicos__boleta')  # Campos por los cuales se podrá buscar
    list_filter = ('firma_asesor','firma_jefe')  # Campos por los cuales se podrá filtrar
    actions = [generar_pdf]


admin.site.register(SolicitudInscripcion, SolicitudInscripcionAdmin)

admin.site.unregister(Group)
admin.site.register(Calendario)
admin.site.register(SolicitudReinscripcion)
admin.site.register(ConstanciaProgramaIndividual)
admin.site.register(ActaRegistroTemaTesis)
admin.site.register(ActaRevisionTesis)
admin.site.register(DatosPersonalesAlumno)
admin.site.register(DatosAcademicosAlumno)
admin.site.register(AntecedentesAcademicos)
admin.site.register(ColegioProfesoresPosgrado)
admin.site.register(DatosAsesor)
admin.site.register(ProgramaActividades)
admin.site.register(ProgramaSemestral)