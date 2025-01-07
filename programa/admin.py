from django.contrib import admin
from .models import *

from .models import UnidadAprendizaje, ProgramaSemestral
from .forms import FormProgramaSemestral

class ProgramaSemestralAdmin(admin.ModelAdmin):
    form = FormProgramaSemestral

class UnidadAprendizajeAdmin(admin.ModelAdmin):
    list_display = ('clave','unidad_aprendizaje','creditos')


admin.site.register(ProgramaSemestral, ProgramaSemestralAdmin)
admin.site.register(UnidadAprendizaje,UnidadAprendizajeAdmin)
admin.site.register(InscripcionPrograma)
admin.site.register(ReinscripcionPrograma)