from django.contrib import admin
from .forms import FormDatosPersonalesAdmin,FormDatosAcademicosAdmin
from .models import *

# Register your models here.
class DatosPersonalesAdmin(admin.ModelAdmin):
    pass
    form = FormDatosPersonalesAdmin
    list_display = ("usuario","nombre_alumno")
    search_fields = ('cuenta__username','cuenta__first_name','cuenta__last_name')
    list_filter = ('cuenta__is_active',)
    # actions = [enviar_informacion_reinscripcion]
    def nombre_alumno(self, obj):
        return f"{obj.cuenta.first_name} {obj.cuenta.last_name}"
    nombre_alumno.short_description = 'Nombre del alumno'
    def usuario(self, obj):
        return f"{obj.cuenta}"
    usuario.short_description = 'Usuario'

class DatosAcademicosAdmin(admin.ModelAdmin):
    pass
    form = FormDatosAcademicosAdmin
    list_display = ("boleta","usuario","nombre_alumno")
    search_fields = ('boleta','cuenta__username','cuenta__first_name','cuenta__last_name')
    list_filter = ('cuenta__is_active',)
    # actions = [enviar_informacion_reinscripcion]
    def nombre_alumno(self, obj):
        return f"{obj.cuenta.first_name} {obj.cuenta.last_name}"
    nombre_alumno.short_description = 'Nombre del alumno'
    def usuario(self, obj):
        return f"{obj.cuenta}"
    usuario.short_description = 'Usuario'

admin.site.register(DatosPersonalesAlumno,DatosPersonalesAdmin)
admin.site.register(DatosAcademicosAlumno,DatosAcademicosAdmin)
