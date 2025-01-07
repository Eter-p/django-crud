from django.db import models
from alumnos.models import DatosAcademicosAlumno,DatosPersonalesAlumno

# COLEGIO_PROFESORES_POSGRADO
class ColegioProfesoresPosgrado(models.Model):
    unidad_colegio_profesores = models.CharField(max_length=255)
    nombre_sesion = models.CharField(max_length=255,null=True,blank=True)
    numero_sesion = models.IntegerField(null=True,blank=True)
    fecha_sesion = models.DateField(default=None,null=True,blank=True)

    def __str__(self):
        return self.nombre_sesion + " No. " + self.numero_sesion
    
    class Meta:
        verbose_name = "Tabla del colegio de profesores"
        verbose_name_plural = "Tabla del colegio de profesores"

# ACTA_REGISTRO_TEMA_TESIS
class ActaRegistroTemaTesis(models.Model):
    datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
    datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
    fecha = models.DateField(default=None,null=True)
    unidad_colegio_profesores = models.CharField(max_length=255,null=True,blank=True)
    nombre_sesion = models.CharField(max_length=255,null=True,blank=True)
    numero_sesion = models.IntegerField(null=True,blank=True)
    fecha_sesion = models.DateField(default=None,null=True,blank=True)
    tema_tesis = models.CharField(max_length=255)
    objetivo_general_tesis = models.TextField()
    nombre_director_1 = models.CharField(max_length=100)
    nombre_director_2 = models.CharField(max_length=100, blank=True, null=True)
    aplicacion_director = models.BooleanField()
    base_tesis = models.TextField()
    firma_director_1 = models.BooleanField(blank=True, null=True)
    firma_director_2 = models.BooleanField(blank=True, null=True)
    firma_alumno = models.BooleanField()
    firma_presidente_colegio = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return f"Acta de Registro de tesis {self.id}"
    
    class Meta:
        verbose_name = "Acta de Registro de Tema de Tesis"
        verbose_name_plural = "Actas de Registro de Tema de Tesis"

# ACTA_REVISION_TESIS
class ActaRevisionTesis(models.Model):
    MANIFIESTO_CHOICE = [
        ('Aprobar', 'Aprobar'),
        ('Susperder', 'Suspender'),
        ('No Aprobar', 'No Aprobar'),
    ]
    datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
    datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
    colegio_profesores = models.ForeignKey(ColegioProfesoresPosgrado, on_delete=models.CASCADE,default=None)
    fecha = models.DateField(default=None)
    titulo_tesis = models.CharField(max_length=255)
    porcentaje_plagio = models.FloatField()
    conclusion_plagio = models.TextField()
    justificacion_conclusion = models.TextField()
    manifiesto_comision = models.TextField(max_length=10,choices=MANIFIESTO_CHOICE)
    firma_director_1 = models.BooleanField(default=None)
    firma_director_2 = models.BooleanField(default=None)
    firma_comision_1 = models.BooleanField()
    firma_comision_2 = models.BooleanField()
    firma_comision_3 = models.BooleanField()
    firma_presidente_colegio = models.BooleanField()

    def __str__(self):
        return f"Acta de Revision de tesis {self.id}"
    
    class Meta:
        verbose_name = "Acta de Revisión de tesis"
        verbose_name_plural = "Actas de Revisión de tesis"
