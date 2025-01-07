from django.db import models
from django.contrib.auth.models import User

# DATOS_PERSONALES_ALUMNO
class DatosPersonalesAlumno(models.Model):
    GENERO_CHOICE = [
        ('H', 'H'),
        ('M', 'M')
    ]
    cuenta = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    calle = models.CharField(max_length=255,blank=True, null=True)
    numero_exterior = models.CharField(max_length=255,blank=True, null=True)
    numero_interior = models.CharField(max_length=255,blank=True, null=True)
    colonia = models.CharField(max_length=255,blank=True, null=True)
    municipio = models.CharField(max_length=255,blank=True, null=True)
    codigo_postal = models.CharField(max_length=255,blank=True, null=True)
    estado = models.CharField(max_length=255,blank=True, null=True)
    pais = models.CharField(max_length=255,blank=True, null=True)
    telefono_casa = models.CharField(max_length=20,blank=True, null=True)
    telefono_movil = models.CharField(max_length=20,blank=True, null=True)
    genero = models.CharField(max_length=1,choices=GENERO_CHOICE,default=None,blank=True, null=True)
    correo_1 = models.EmailField(blank=True, null=True)
    correo_2 = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.cuenta.first_name} {self.cuenta.last_name}"
    
    class Meta:
        verbose_name = "Datos personales"
        verbose_name_plural = "Datos personales"
    
# DATOS_ACADEMICOS_ALUMNO
class DatosAcademicosAlumno(models.Model):
    ESTATUS_CHOICE = [
        ('Completo', 'Tiempo Completo'),
        ('Parcial', 'Tiempo Parcial'),
    ]
    cuenta = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    boleta = models.CharField(max_length=50,blank=True,null=True)
    unidad_academica_actual = models.CharField(max_length=100,blank=True,null=True,default="ESCOM")
    nom_programa_actual = models.CharField(max_length=100,blank=True,null=True)
    estatus = models.CharField(max_length=8, choices=ESTATUS_CHOICE, default='Completo',blank=True,null=True)

    def __str__(self):
        return f"{self.boleta}"

    class Meta:
        verbose_name = "Datos Académicos"
        verbose_name_plural = "Datos Académicos"
