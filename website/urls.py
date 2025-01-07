"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views_f. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views_f
    1. Add an import:  from my_app import views_f
    2. Add a URL to urlpatterns:  path('', views_f.home, name='home')
Class-based views_f
    1. Add an import:  from other_app.views_f import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from alumnos import views as views_a
from calendarios import views as views_c
from formularios import views as views_f
from formularios.utils import failure
from programa import views as views_p

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views_f.signin,name='index'),
    path('actualizacion/datos/personales',views_a.registro_datos_p,name='actpersonales'),
    path('actualizacion/datos/academicos',views_a.registro_datos_a,name='actacademicos'),
    path('formularios/',views_c.info_formularios,name='formularios'),
	path('solicitud/inscripcion/datos/alumno', views_f.inscripcion_datos,name='inscripcion_datos'),
	path('solicitud/inscripcion/antecedentes', views_f.inscripcion_antecedentes,name='inscripcion_antecedentes'),
	path('solicitud/inscripcion/programa', views_f.inscripcion_programa,name='inscripcion_programa'),
	path('solicitud/inscripcion/firmas', views_f.inscripcion_firmas,name='inscripcion_firmas'),
	path('solicitud/inscripcion/firmas/pendiente', views_f.inscripcion_firmas_pendiente,name='inscripcion_firmas_pendiente'),
	path('solicitud/cancelar', views_f.solicitud_cancelar,name='solicitud_cancelar'),
	# path('solicitud/reinscripcion', views_f.reinscripcion,name='reinscripcion'),
	# path('programa/individual/actividades', views_f.programa_actividades,name='programa_actividades'),
	# path('tesis/registro', views_f.tesis_registro,name='tesis_registro'),
	# path('tesis/revision', views_f.tesis_revision,name='tesis_revision'),
    path('logout/',views_f.signout,name='logout'),
    path('success/<str:tipo>',views_f.success,name='success'),
    path('failure/<str:tipo>',failure,name='failure'),
    path('superusuario/', views_f.crear_superusuario, name='crear_superusuario'),
    path('calendario/', views_c.creacion_calendario, name='creacion_calendario'),
    path('programa/', views_p.unidades_apendizaje, name='unidades_apendizaje'),
    path('pdf/', views_f.generar_pdf, name='generar_pdf'),
]