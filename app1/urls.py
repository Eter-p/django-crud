from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('projects/', views.projects,name='project'),
	path('tasks/', views.tasks, name='tasks'),
	path('tasks/create/', views.create_task, name='create_tasks'),
	path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
	path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
	path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('signup/',views.signup),
    path('signin/',views.signin,name='signin'),
    path('logout/',views.signout),
]