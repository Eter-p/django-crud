from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group,User
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *
from .utils import informacion_inscripcion,informacion_reinscripcion

from alumnos.admin import DatosPersonalesInLine
admin.site.site_title = "SEPI - Administración"
admin.site.site_header = "Panel de Administración"
admin.site.index_title = "Bienvenido al Administrador"

class CustomUserAdmin(UserAdmin):
    inlines = [DatosPersonalesInLine]
    extra = 0
    form = CustomUserChangeForm
    list_display = ("username",'email','first_name','last_name','is_docente')
    def is_docente(self, obj):
        if obj.is_staff:
            return f"✅"
        return f"❌"
    is_docente.short_description = 'Es Docente'

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if not request.user.is_superuser:
            fieldsets = [(name, {'fields': fields}) for name, fields in fieldsets if name != 'Permisos']
        return fieldsets


def enviar_informacion_inscripcion(modeladmin,request, queryset):
    try:
        datos_formularios = []
        for obj in queryset:
            datos_formularios.append(informacion_inscripcion(obj))
        return render(request,"pdfs/lanzador.html",{'datos': datos_formularios})
    except Exception as error:
        return HttpResponse(f'Error al enviar los datos el PDF{error}')
enviar_informacion_inscripcion.short_description = "Ver reporte en una nueva pagina"

class SolicitudInscripcionAdmin(admin.ModelAdmin):
    form = FormSolicitudInscripcionAdmin
    list_display = ('id',"nombre_completo",'firma_asesor','nombre_asesor','firma_jefe','nombre_jefe')
    search_fields = ('datos_personales__cuenta__first_name','datos_personales__cuenta__last_name','asesor__first_name','asesor__last_name')
    list_filter = ('firma_asesor','firma_jefe')
    actions = [enviar_informacion_inscripcion]
    def nombre_completo(self, obj):
        return f"{obj.datos_personales.cuenta.first_name} {obj.datos_personales.cuenta.last_name}"
    def nombre_asesor(self, obj):
        return f"{obj.asesor.first_name} {obj.asesor.last_name}"
    def nombre_jefe(self, obj):
        return f"{obj.jefe.first_name} {obj.jefe.last_name}"
    nombre_completo.short_description = 'Nombre Completo'

def enviar_informacion_reinscripcion(modeladmin,request, queryset):
    try:
        datos_formularios = []
        for obj in queryset:
            datos_formularios.append(informacion_reinscripcion(obj))
        return render(request,"pdfs/lanzador.html",{'datos': datos_formularios})
    except Exception as error:
        return HttpResponse(f'Error al enviar los datos el PDF{error}')
enviar_informacion_reinscripcion.short_description = "Ver reporte en una nueva pagina"

class SolicitudReinscripcionAdmin(admin.ModelAdmin):
    form = FormSolicitudReinscripcionAdmin
    list_display = ('id',"nombre_completo",'firma_asesor','nombre_asesor','firma_jefe','nombre_jefe')
    search_fields = ('datos_personales__cuenta__first_name','datos_personales__cuenta__last_name','asesor__first_name','asesor__last_name')
    list_filter = ('firma_asesor','firma_jefe')
    actions = [enviar_informacion_reinscripcion]
    def nombre_completo(self, obj):
        return f"{obj.datos_personales.cuenta.first_name} {obj.datos_personales.cuenta.last_name}"
    def nombre_asesor(self, obj):
        return f"{obj.asesor.first_name} {obj.asesor.last_name}"
    def nombre_jefe(self, obj):
        return f"{obj.jefe.first_name} {obj.jefe.last_name}"
    nombre_completo.short_description = 'Nombre Completo'

class InscripcionAntecedentesAdmin(admin.ModelAdmin):
    list_display = ('id_solicitud_inscripcion', 'id_antecedentes')
    # actions = [enviar_informacion]

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(SolicitudInscripcion,SolicitudInscripcionAdmin)
admin.site.register(SolicitudReinscripcion, SolicitudReinscripcionAdmin)
admin.site.register(InscripcionAntecedentes, InscripcionAntecedentesAdmin)

admin.site.register(ConstanciaProgramaIndividual)
admin.site.register(AntecedentesAcademicos)
