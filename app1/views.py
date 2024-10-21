from django.http import HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
#from .models import Project, Task
#from .forms import TaskForm

# Create your views here.
# def index(request):
# 	return render(request, "index.html")

# def signup(request):
# 	if request.method == "GET":
# 		return render(request,"signup.html", {
# 			"form": UserCreationForm 
# 		})
# 	else:
# 		if request.POST["password1"] == request.POST["password2"]:
# 			try:
# 				user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
# 				user.save()
# 				login(request,user)
# 				return redirect("tasks")
# 			except:
# 				return render(request,"signup.html", {
# 					"form": UserCreationForm,
# 					"error": "Error al crear usuario"
# 				})
# 		return render(request,"signup.html", {
# 			"form": UserCreationForm,
# 			"error": "Las contraseñas no coinciden"
# 		})

# @login_required
# def signout(request):
# 	logout(request)
# 	return redirect("index")

# def signin(request):
# 	if request.method == "GET":
# 		return render(request, "signin.html",{
# 			'form': AuthenticationForm
# 		})
# 	else:
# 		user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
# 		if user is None:
# 			return render(request, "signin.html",{
# 				'form': AuthenticationForm,
# 				'error': "Usuario o contraseña incorrecto"
# 			})
# 		else:
# 			login(request,user)
# 			return redirect('tasks')

# @login_required
# def projects(request):
# 	proys = Project.objects.all()
# 	return render(request,"projects.html",{'proyectos':proys})

# @login_required
# def tasks(request):
# #	tareas = Task.objects.all()
# 	tareas = Task.objects.filter(user=request.user,datecompleted__isnull = True)
# 	return render(request,"tasks.html",{'tareas':tareas})

# @login_required
# def create_task(request):
# 	if request.method == "GET":
# 		return render(request,"create_task.html",{
# 			'form': TaskForm
# 		})
# 	else:
# 		try:
# 			form = TaskForm(request.POST)
# 			new_task = form.save(commit=False)
# 			new_task.user = request.user
# 			new_task.save()
# 			return redirect('tasks')
# 		except:
# 			return render(request,"create_task.html",{
# 				'form': TaskForm,
# 				'error': "problema al crear la tarea"
# 			})

# @login_required
# def task_detail(request, task_id):
# 	task = get_object_or_404(Task,pk=task_id,user = request.user)
# 	if request.method == 'GET':
# 		form = TaskForm(instance=task)
# 		return render(request,"task_detail.html",{'task':task,'form':form})
# 	else:
# 		try:
# 			form = TaskForm(request.POST,instance=task)
# 			form.save()
# 			return redirect('tasks')
# 		except:
# 			return render(request,"task_detail.html",{
# 				'task':task,
# 				'form':form,
# 				'error': "Error al actualizar los datos"}
# 			)

# @login_required
# def complete_task(request,task_id):
# 	task = get_object_or_404(Task,pk=task_id,user=request.user)
# 	if  request.method == 'POST':
# 		task.datecompleted = timezone.now()
# 		task.save()
# 		return redirect('tasks')
	
# @login_required
# def delete_task(request,task_id):
	# task = get_object_or_404(Task,pk=task_id,user=request.user)
	# if  request.method == 'POST':
	# 	task.delete()
	# 	return redirect('tasks')
