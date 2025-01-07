from django.db import models
from django.contrib.auth.models import User
from alumnos.models import DatosAcademicosAlumno,DatosPersonalesAlumno

# SOLICITUD_INSCRIPCION
class SolicitudInscripcion(models.Model):
    datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE,blank=True,null=True)
    datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE,blank=True,null=True)
    fecha = models.DateField(null=True,blank=True)
    asesor = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="profesor_asesor_inscripcion")
    jefe = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="profesor_jefe_inscripcion")
    firma_alumno = models.BooleanField(null=True,blank=True)
    firma_asesor = models.BooleanField(null=True,blank=True)
    firma_jefe = models.BooleanField(null=True,blank=True)
    aviso_privacidad = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return f"id. Inscripción {self.id} : {self.datos_personales}"
    
    class Meta:
        verbose_name = "Solicitud de Inscripción"
        verbose_name_plural = "Solicitudes de Inscripción"
    
# ANTECEDENTES_ACADEMICOS
class AntecedentesAcademicos(models.Model):
    NIVEL_CHOICE = [
        ('Licenciatura', 'Licenciatura'),
        ('Especialidad', 'Especialidad'),
        ('Maestria', 'Maestria'),
        ('Doctorado', 'Doctorado'),
    ]
    nivel_academico_cursado = models.CharField(max_length=12,choices=NIVEL_CHOICE,default='Licenciatura')
    programa_academico_cursado = models.CharField(max_length=100)
    institucion_donde_curso = models.CharField(max_length=255,default="ESCOM")
    estado_institucion = models.CharField(max_length=100)
    fecha_graduacion = models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.id} : {self.nivel_academico_cursado} - {self.programa_academico_cursado}"
    
    class Meta:
        verbose_name = "Tabla de Antecedentes Académicos"
        verbose_name_plural = "Tabla de Antecedentes Académicos"

# INSCRIPCION_ANTECEDENTES
class InscripcionAntecedentes(models.Model):
    id_solicitud_inscripcion = models.ForeignKey(SolicitudInscripcion,on_delete=models.CASCADE)
    id_antecedentes = models.ForeignKey(AntecedentesAcademicos,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
    class Meta:
        verbose_name = "Solicitud de incripción - Antecedentes"
        verbose_name_plural = "Tabla Solicitudes de incripción - Antecedentes"

# SOLICITUD_REINSCRIPCION
class SolicitudReinscripcion(models.Model):
    SEMESTRE_CHOICE = [
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9')
    ]
    datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE,blank=True,null=True)
    datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE,blank=True,null=True)
    fecha = models.DateField(blank=True,null=True)
    periodo = models.CharField(max_length=50)
    semestre_a_cursar = models.IntegerField(blank=True,null=True,choices=SEMESTRE_CHOICE)
    requiere_unidad = models.BooleanField(null=True,blank=True)
    jefe = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="profesor_jefe_reinscripcion")
    asesor = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="profesor_asesor_reinscripcion")
    firma_alumno = models.BooleanField(null=True,blank=True)
    firma_asesor = models.BooleanField(null=True,blank=True)
    firma_jefe = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return f"id. Reinscripción {self.id} : {self.datos_personales}"
    
    class Meta:
        verbose_name = "Solicitud de Reinscripción"
        verbose_name_plural = "Solicitudes de Reinscripción"

# CONSTANCIA_PROGRAMA_INDIVIDUAL
class ConstanciaProgramaIndividual(models.Model):
    datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
    datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
    fecha = models.DateField()
    asesor = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name="profesor_asesor_programa_individual")
    fecha_limite = models.DateField(null=True)
    firma_alumno = models.BooleanField()
    firma_asesor = models.BooleanField()
    firma_jefe = models.BooleanField()

    def __str__(self):
        return f"Constancia {self.id}"
    
    class Meta:
        verbose_name = "Constancia de inscripción al programa individual"
        verbose_name_plural = "Constancias de inscripción al programa individual"
