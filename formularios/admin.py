from django.contrib import admin
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render
from .models import *

admin.site.site_title = "SEPI - Administración"
admin.site.site_header = "Panel de Administración"
admin.site.index_title = "Bienvenido al Administrador"

def enviar_informacion(modeladmin,request, queryset):
        try:
            datos = []
            for obj in queryset:
                datos.append({
                    'apellido_paterno': obj.datos_personales.apellido_paterno,
                    'apellido_materno': obj.datos_personales.apellido_materno,
                    'nombre': obj.datos_personales.nombre,
                    'calle': obj.datos_personales.calle,
                    'numero_exterior': obj.datos_personales.numero_exterior,
                    'numero_interior': obj.datos_personales.numero_interior,
                    'colonia': obj.datos_personales.colonia,
                    'municipio': obj.datos_personales.municipio,
                    'codigo_postal': obj.datos_personales.codigo_postal,
                    'estado': obj.datos_personales.estado,
                    'telefono_casa': obj.datos_personales.telefono_casa,
                    'telefono_movil': obj.datos_personales.telefono_movil,
                    'genero': obj.datos_personales.genero,
                    'correo_1': obj.datos_personales.correo_1,
                    'correo_2': obj.datos_personales.correo_2,
                    'unidad_academica_actual': obj.datos_academicos.unidad_academica_actual,
                    'nom_programa_actual': obj.datos_academicos.nom_programa_actual,
                    'estatus': obj.datos_academicos.estatus,
                    'antecedentes': dict_antecedentes(obj.id),
                    'programa': dict_programa(obj.id),
                    'asesor': obj.asesor,
                    'jefe': obj.jefe,
                    'aviso_privacidad': obj.aviso_privacidad,
                    'fecha': obj.fecha.strftime("%d/%m/%Y")
                })
            return render(request,"pdfs/lanzador.html",{'datos': datos})
        except Exception as error:
            return HttpResponse(f'Error al enviar los datos el PDF{error}')
enviar_informacion.short_description = "Ver reporte en una nueva pagina"

def dict_antecedentes(id):
    enlaces = InscripcionAntecedentes.objects.filter(id_solicitud_inscripcion=id)
    antecedentes = []

    contador = 2
    for enlace in enlaces:
        antecedente = AntecedentesAcademicos.objects.get(id=enlace.id_antecedentes.id)
        datos_antecedente = {}
        datos_antecedente["indice"] = contador
        datos_antecedente["nivel_academico_cursado"] = antecedente.nivel_academico_cursado
        datos_antecedente["programa_academico_cursado"] = antecedente.programa_academico_cursado
        datos_antecedente["institucion_donde_curso"] = antecedente.institucion_donde_curso
        datos_antecedente["estado_institucion"] = antecedente.estado_institucion
        datos_antecedente["fecha_graduacion"] = antecedente.fecha_graduacion.strftime("%d/%m/%Y")
        antecedentes.append(datos_antecedente)
        contador = contador+1
    return str(antecedentes)

def dict_programa(id):
    enlaces = InscripcionPrograma.objects.filter(id_solicitud_inscripcion=id)
    programa = []

    contador = 2
    for enlace in enlaces:        
        materia = ProgramaSemestral.objects.get(id=enlace.id_programa_semestral.id)
        datos_materia = {}
        datos_materia["indice"] = contador
        datos_materia["clave"] = materia.clave
        datos_materia["unidad_aprendizaje"] = materia.unidad_aprendizaje
        datos_materia["profesor"] = materia.profesor
        datos_materia["lugar_realizacion"] = materia.lugar_realizacion
        programa.append(datos_materia)
        contador = contador+1
    return str(programa)

class SolicitudInscripcionAdmin(admin.ModelAdmin):
    list_display = ('datos_personales', 'datos_academicos','firma_asesor','asesor','firma_jefe','jefe')
    search_fields = ('datos_personales__nombre','datos_personales__apellido_paterno','datos_personales__apellido_materno', 'datos_academicos__boleta')  # Campos por los cuales se podrá buscar
    list_filter = ('firma_asesor','firma_jefe')
    actions = [enviar_informacion]

class SolicitudReinscripcionAdmin(admin.ModelAdmin):
    list_display = ('datos_personales', 'datos_academicos','firma_asesor','firma_jefe')
    search_fields = ('datos_personales__nombre','datos_personales__apellido_paterno','datos_personales__apellido_materno', 'datos_academicos__boleta')  # Campos por los cuales se podrá buscar
    list_filter = ('firma_asesor','firma_jefe')
    actions = [enviar_informacion]

class InscripcionAntecedentesAdmin(admin.ModelAdmin):
    list_display = ('id_solicitud_inscripcion', 'id_antecedentes')
    actions = [enviar_informacion]

class InscripcionProgramaAdmin(admin.ModelAdmin):
    list_display = ('id_solicitud_inscripcion', 'id_programa_semestral')
    actions = [enviar_informacion]

admin.site.register(SolicitudInscripcion, SolicitudInscripcionAdmin)
admin.site.register(SolicitudReinscripcion, SolicitudReinscripcionAdmin)
admin.site.register(InscripcionAntecedentes, InscripcionAntecedentesAdmin)
admin.site.register(InscripcionPrograma, InscripcionProgramaAdmin)

admin.site.unregister(Group)
admin.site.register(Calendario)
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