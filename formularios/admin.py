from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *

admin.site.site_title = "SEPI - Administración"
admin.site.site_header = "Panel de Administración"
admin.site.index_title = "Bienvenido al Administrador"


class SolicitudInscripcionAdmin(admin.ModelAdmin):
    list_display = ('datos_personales', 'datos_academicos','firma_asesor','firma_jefe')  # Campos que se mostrarán en la lista
    search_fields = ('datos_personales__nombre','datos_personales__apellido_paterno','datos_personales__apellido_materno', 'datos_academicos__boleta')  # Campos por los cuales se podrá buscar
    list_filter = ('firma_asesor','firma_jefe')  # Campos por los cuales se podrá filtrar

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