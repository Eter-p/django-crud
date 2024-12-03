"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from formularios import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('formularios/',views.formularios,name='formularios'),
	path('solicitud/inscripcion/datos/alumno', views.inscripcion_datos,name='inscripcion_datos'),
	path('solicitud/inscripcion/antecedentes', views.inscripcion_antecedentes,name='inscripcion_antecedentes'),
	path('solicitud/inscripcion/programa', views.inscripcion_programa,name='inscripcion_programa'),
	path('solicitud/inscripcion/firmas', views.inscripcion_firmas,name='inscripcion_firmas'),
	path('solicitud/reinscripcion', views.reinscripcion,name='reinscripcion'),
	path('programa/individual/actividades', views.programa_actividades,name='programa_actividades'),
	path('solicitud/cancelar', views.solicitud_cancelar,name='solicitud_cancelar'),
	path('tesis/registro', views.tesis_registro,name='tesis_registro'),
	path('tesis/revision', views.tesis_revision,name='tesis_revision'),
	# path('tasks/', views.tasks, name='tasks'),
	# path('tasks/create/', views.create_task, name='create_tasks'),
	# path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
	# path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
	# path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.signout,name='logout'),
    path('success/<str:folio>',views.success,name='success'),
]
