from django.shortcuts import render
from .models import UnidadAprendizaje
from django.shortcuts import render,redirect

# Create your views here.
def unidades_apendizaje(request):
    if len(UnidadAprendizaje.objects.all())==0:
        UnidadAprendizaje.objects.create(
            clave = "09B5786",
            unidad_aprendizaje = "Métodos matemáticos para el análisis de sistemas y señales",
            creditos = 6
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5787",
            unidad_aprendizaje = "Fundamentos de comunicaciones móviles	5",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5789",
            unidad_aprendizaje = "Seminario I",
            creditos = 2
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5791",
            unidad_aprendizaje = "Arquitectura de dispositivos móviles",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "05B4670",
            unidad_aprendizaje = "Trabajo tesis",
            creditos = 0
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5792",
            unidad_aprendizaje = "Seminario II",
            creditos = 2
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5794",
            unidad_aprendizaje = "Seminario III",
            creditos = 3
        )
        UnidadAprendizaje.objects.create(
            clave = "13A6641",
            unidad_aprendizaje = "Seminario IV",
            creditos = 3
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5813",
            unidad_aprendizaje = "Visión computacional",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5812",
            unidad_aprendizaje = "Realidad virtual",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5793",
            unidad_aprendizaje = "Sistemas operativos para cómputo móvil",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5808",
            unidad_aprendizaje = "Ingeniería de software para el cómputo móvil",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5806",
            unidad_aprendizaje = "Tópicos en inteligencia artificial actual",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5814",
            unidad_aprendizaje = "Cómputo educativo y multimedios móviles",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5810",
            unidad_aprendizaje = "Gestión de proyectos de cómputo móvil",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5799",
            unidad_aprendizaje = "Modelos combinatorios para sistemas de dispositivos móviles",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5807",
            unidad_aprendizaje = "Calidad en el servicio en sistemas móviles",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5803",
            unidad_aprendizaje = "Comunicaciones a distancia",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5804",
            unidad_aprendizaje = "Estadistica en comunicaciones",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "12B6546",
            unidad_aprendizaje = "Análisis de teletráfico en redes de cómputo móvil",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5802",
            unidad_aprendizaje = "Tópicos selectos de comunicaciones avanzadas",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5809",
            unidad_aprendizaje = "Seguridad en redes inalámbricas",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5805",
            unidad_aprendizaje = "Redes inalámbricas",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5801",
            unidad_aprendizaje = "Procesamiento de señales de video y T.V. móvil",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5797",
            unidad_aprendizaje = "Programación de dispositivos de hardware",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "11A6264",
            unidad_aprendizaje = "Sistemas de tiempo real",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5788",
            unidad_aprendizaje = "Programación de dispositivos de altas prestaciones",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5790",
            unidad_aprendizaje = "Programación de dispositivos móviles",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5795",
            unidad_aprendizaje = "Diseño de sistemas digitales aplicados al cómputo móvil",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5796",
            unidad_aprendizaje = "Mecanismos controlados por dispositivos móviles",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5800",
            unidad_aprendizaje = "Tópicos selectos de procesamiento de señales de voz en cómputo móvil",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "09B5811",
            unidad_aprendizaje = "Multimedios orientados a dispositivos móviles	",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "12B6546",
            unidad_aprendizaje = "Sistemas computacionales para el análisis de componentes independientes",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "15B7351",
            unidad_aprendizaje = "Mobile Commerce",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "15B7352",
            unidad_aprendizaje = "Cloud Computing",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "15B7353",
            unidad_aprendizaje = "Cellular Systems",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "17B7354",
            unidad_aprendizaje = "Security in Mobile Systems",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "17B7355",
            unidad_aprendizaje = "Multirate Digital Signal Processing",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "15B7356",
            unidad_aprendizaje = "Mobile E - Business",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "15B7357",
            unidad_aprendizaje = "Mobile Computing Technologies Proyect Management",
            creditos = 5
        )
        UnidadAprendizaje.objects.create(
            clave = "15B7355",
            unidad_aprendizaje = "Embedded Systems",
            creditos = 5
        )
        return redirect("success","0")
    return redirect("failure","0")