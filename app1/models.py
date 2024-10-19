from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Administrador (models.Model):
	usuario = models.CharField(max_length = 200)
	def __str__(self) -> str:
		return self.usuario

class Project(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self) -> str:
		return self.name

class Task(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	created = models.DateTimeField(auto_now=True)
	datecompleted= models.DateField(null=True,blank=True)
	important = models.BooleanField(default=False)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	project = models.ForeignKey(Project,on_delete=models.CASCADE)

	def __str__(self) -> str:
		return self.title


class DatosPAlumno (models.Model):
	nombre = models.CharField(max_length = 200)
	apellido_materno = models.CharField(max_length = 200)
	apellido_paterno = models.CharField(max_length = 200)
	fecha_de_nacimiento = models.TextField()
	domicilio = models.TextField()
	telefono_casa = models.CharField(max_length = 200)
	telefono_movil = models.CharField(max_length = 200)
	sexo = models.CharField(max_length = 200)
	correo_1 = models.CharField(max_length = 200)
	correo_2 = models.CharField(max_length = 200)

	def __str__(self) -> str:
		return self.apellido_materno + self.apellido_paterno + self.nombre
