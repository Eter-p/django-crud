from .forms import InscripcionAntecedentes,AntecedentesAcademicos
from programa.models import InscripcionPrograma,ProgramaSemestral
from django.shortcuts import render,redirect,get_object_or_404
from django.core.mail import send_mail
from datetime import datetime

form_solicitud = None
correo = ""
control = True

def comprueba_firma(dato):
	if dato == None:
		return False
	else:
		return "on" in dato

def fecha_mayor(fecha_solicitud, fecha_convocatoria):
    formato = "%Y-%m-%d %H:%M:%S"
    fecha_solicitud = datetime.strptime(fecha_solicitud, formato)
    fecha_convocatoria = datetime.strptime(fecha_convocatoria, formato)
    return fecha_solicitud > fecha_convocatoria

def failure(request,tipo):
	if request.method == "GET":
		return render(request,"responseHTML/failure.html",{'tipo': tipo})
	try:
		opcion = request.POST.get("control")
		if opcion == "modificar":
			if tipo == "1":
				return redirect("inscripcion_datos")
			if tipo == "2":
				print("20")
				return redirect("reinscripcion")
		return redirect("index")
	except Exception as error:
		return render(request,"failure",{'falla': tipo,"error":error})

def enviar_correo(id,tipo):
	asunto = tipo
	mensaje = "Guarda este numero y entregalo a los profesores correspondientes: "+str(id)
	destinatario = correo
	send_mail(
		asunto,
		mensaje,
		'hernandez.hernandez.fabian@gmail.com',  # Desde este correo
		[destinatario],  # A este correo
		fail_silently=False,
	)

def informacion_inscripcion(obj):
	apellido = f'{obj.datos_personales.cuenta.last_name}'.split()
	datos_ins = {
		'tipo':"Solicitud_Inscripcion",
		'apellido_paterno': apellido[0],
		'apellido_materno': apellido[-1],
		'nombre': obj.datos_personales.cuenta.first_name,
		'calle': obj.datos_personales.calle,
		'numero_exterior': obj.datos_personales.numero_exterior,
		'numero_interior': obj.datos_personales.numero_interior,
		'colonia': obj.datos_personales.colonia,
		'municipio': obj.datos_personales.municipio,
		'codigo_postal': obj.datos_personales.codigo_postal,
		'estado': obj.datos_personales.estado,
		'pais': obj.datos_personales.pais,
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
		'asesor': f'{obj.asesor.first_name} {obj.asesor.last_name}',
		'firma_asesor': obj.firma_asesor,
		'jefe': f'{obj.jefe.first_name} {obj.jefe.last_name}',
		'firma_jefe': obj.firma_jefe,
		'aviso_privacidad': obj.aviso_privacidad,
		'fecha': obj.fecha.strftime("%d/%m/%Y")
	}
	return datos_ins

def informacion_reinscripcion(obj):
	apellido = f'{obj.datos_personales.cuenta.last_name}'.split()
	datos_reins = {
		'tipo':"Solicitud_Reinscripcion",
		'fecha': obj.fecha.strftime("%d/%m/%Y"),
		'apellido_paterno': apellido[0],
		'apellido_materno': apellido[-1],
		'nombre': obj.datos_personales.cuenta.first_name,
		'boleta': obj.datos_academicos.boleta,
		'estatus': obj.datos_academicos.estatus,
		'unidad_academica_actual': obj.datos_academicos.unidad_academica_actual,
		'periodo': obj.periodo,
		'semestre': obj.semestre_a_cursar,
		'requiere_unidad': obj.requiere_unidad,
		'nom_programa_actual': obj.datos_academicos.nom_programa_actual,
		'programa': dict_programa(obj.id),
		'asesor': f'{obj.asesor.first_name} {obj.asesor.last_name}',
		'firma_asesor': obj.firma_asesor,
		'jefe': f'{obj.jefe.first_name} {obj.jefe.last_name}',
		'firma_jefe': obj.firma_jefe,
	}
	return datos_reins

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
        datos_materia["clave"] = materia.unidad_aprendizaje.clave
        datos_materia["unidad_aprendizaje"] = materia.unidad_aprendizaje.unidad_aprendizaje
        datos_materia["profesor"] = f'{materia.profesor.first_name} {materia.profesor.last_name}'
        datos_materia["lugar_realizacion"] = materia.lugar_realizacion
        programa.append(datos_materia)
        contador = contador+1
    return str(programa)