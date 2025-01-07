from django.contrib import admin
from .forms import FormDatosPersonalesAdmin,FormDatosAcademicosAdmin
from .models import *
from formularios.models import SolicitudInscripcion,SolicitudReinscripcion

class InscripcionInLine(admin.StackedInline):
    model = SolicitudInscripcion
    extra = 0

class ReinscripcionInLine(admin.StackedInline):
    model = SolicitudReinscripcion
    extra = 0

class DatosPersonalesInLine(admin.StackedInline):
    model = DatosPersonalesAlumno
    extra = 0
    inlines = [InscripcionInLine,ReinscripcionInLine]

class DatosPersonalesAdmin(admin.ModelAdmin):
    extra = 0
    inlines = [InscripcionInLine,ReinscripcionInLine]
    form = FormDatosPersonalesAdmin
    list_display = ("usuario","nombre_alumno")
    search_fields = ('cuenta__username','cuenta__first_name','cuenta__last_name')
    list_filter = ('cuenta__is_active',)
    def nombre_alumno(self, obj):
        return f"{obj.cuenta.first_name} {obj.cuenta.last_name}"
    nombre_alumno.short_description = 'Nombre del alumno'
    def usuario(self, obj):
        return f"{obj.cuenta}"
    usuario.short_description = 'Usuario'

class DatosAcademicosAdmin(admin.ModelAdmin):
    extra = 0
    inlines = [InscripcionInLine,ReinscripcionInLine]
    form = FormDatosAcademicosAdmin
    list_display = ("boleta","usuario","nombre_alumno")
    search_fields = ('boleta','cuenta__username','cuenta__first_name','cuenta__last_name')
    list_filter = ('cuenta__is_active',)
    def nombre_alumno(self, obj):
        return f"{obj.cuenta.first_name} {obj.cuenta.last_name}"
    nombre_alumno.short_description = 'Nombre del alumno'
    def usuario(self, obj):
        return f"{obj.cuenta}"
    usuario.short_description = 'Usuario'

admin.site.register(DatosPersonalesAlumno,DatosPersonalesAdmin)
admin.site.register(DatosAcademicosAlumno,DatosAcademicosAdmin)
