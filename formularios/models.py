from django.db import models
from django.db import models

# DATOS_PERSONALES_ALUMNO
class DatosPersonalesAlumno(models.Model):
    GENERO_CHOICE = [
        ('H', 'H'),
        ('M', 'M')
    ]
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=255,blank=True, null=True)
    telefono_casa = models.CharField(max_length=20,blank=True, null=True)
    telefono_movil = models.CharField(max_length=20,blank=True, null=True)
    genero = models.CharField(max_length=1,choices=GENERO_CHOICE,default=None,blank=True, null=True)
    correo_1 = models.EmailField(blank=True, null=True)
    correo_2 = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.apellido_paterno} {self.apellido_materno} {self.nombre}"
    
# DATOS_ACADEMICOS_ALUMNO
class DatosAcademicosAlumno(models.Model):
    ESTATUS_CHOICE = [
        ('Completo', 'Tiempo Completo'),
        ('Parcial', 'Tiempo Parcial'),
    ]
    boleta = models.CharField(max_length=50,blank=True,null=True)
    unidad_academica_actual = models.CharField(max_length=100,blank=True,null=True)
    nom_programa_actual = models.CharField(max_length=100)
    estatus = models.CharField(max_length=8, choices=ESTATUS_CHOICE, default='Completo',blank=True,null=True)

    def __str__(self):
        if {self.boleta}!=None:
            return f"{self.boleta}"
        else:
            return f"Sin boleta {self.id}"

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
    institucion_donde_curso = models.CharField(max_length=255)
    estado_institucion = models.CharField(max_length=100)
    fecha_graduacion = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.programa_academico_cursado

# PROGRAMA_SEMESTRAL
class ProgramaSemestral(models.Model):
    UNIDADES = [
        ("09B5786","Métodos matemáticos para el análisis de sistemas y señales"),
        ("09B5787","Fundamentos de comunicaciones móviles"),
        ("O1","Optativa I"),
        ("09B5789","Seminario I"),
        ("09B5791","Arquitectura de dispositivos móviles"),
        ("O2","Optativa II"),
        ("05B4670","Trabajo tesis"),
        ("09B5792","Seminario II"),
        ("O3","Optativa III"),
        ("O4","Optativa IV"),
        ("05B4670","Trabajo tesis"),
        ("09B5794","Seminario III"),
        ("13A6641","Seminario IV"),
        ("TESIS","Tesis")
    ]
    clave = models.CharField(max_length=50)
    unidad_aprendizaje = models.CharField(max_length=100,choices=UNIDADES,default="el")
    profesor = models.CharField(max_length=100)
    lugar_realizacion = models.CharField(max_length=255,default="ESCOM")

    def __str__(self):
        return self.unidad_aprendizaje

# SOLICITUD_INSCRIPCION
class SolicitudInscripcion(models.Model):
    datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
    datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
    firma_alumno = models.BooleanField(null=True,blank=True)
    firma_asesor = models.BooleanField(null=True,blank=True)
    firma_jefe = models.BooleanField(null=True,blank=True)
    aviso_privacidad = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return f"Solicitud de Inscripción {self.id} : {self.datos_personales} - {self.datos_academicos}"
    
    class Meta:
        verbose_name = "Solicitud de Inscripción"
        verbose_name_plural = "Solicitudes de Inscripción"
    

# INSCRIPCION_ANTECEDENTES
class InscripcionAntecedentes(models.Model):
    id_solicitud_inscripcion = models.ForeignKey(SolicitudInscripcion,on_delete=models.CASCADE)
    id_antecedentes = models.ForeignKey(AntecedentesAcademicos,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

# INSCRIPCION_PROGRAMA
class InscripcionPrograma(models.Model):
    id_solicitud_inscripcion = models.ForeignKey(SolicitudInscripcion,on_delete=models.CASCADE)
    id_programa_semestral = models.ForeignKey(ProgramaSemestral,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

# SOLICITUD_REINSCRIPCION
class SolicitudReinscripcion(models.Model):
    NIVEL_CHOICE = [
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
    ]
    datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
    datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
    fecha = models.DateField()
    periodo = models.CharField(max_length=50)
    semestre_a_cursar = models.IntegerField(choices=NIVEL_CHOICE)
    requiere_unidad = models.BooleanField()
    firma_alumno = models.BooleanField()
    firma_asesor = models.BooleanField(null=True,blank=True)
    firma_jefe = models.BooleanField(null=True,blank=True)

    def __str__(self):
        return f"Solicitud Reinscripción {self.id}"
    
    class Meta:
        verbose_name = "Solicitud de Reinscripción"
        verbose_name_plural = "Solicitudes de Reinscripción"

# REINSCRIPCION_PROGRAMA
class ReinscripcionPrograma(models.Model):
    id_solicitud_reinscripcion = models.ForeignKey(SolicitudReinscripcion,on_delete=models.CASCADE)
    id_programa_semestral = models.ForeignKey(ProgramaSemestral,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"

# DATOS_ASESOR
class DatosAsesor(models.Model):
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.apellido_paterno} {self.apellido_materno} {self.nombre}"

# CONSTANCIA_PROGRAMA_INDIVIDUAL
class ConstanciaProgramaIndividual(models.Model):
    datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
    datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
    asesor = models.ForeignKey(DatosAsesor, on_delete=models.CASCADE)
    fecha = models.DateField()
    total_creditos = models.FloatField(null=True)
    fecha_limite = models.DateField(null=True)
    firma_alumno = models.BooleanField()
    firma_asesor = models.BooleanField()
    firma_jefe = models.BooleanField()

    def __str__(self):
        return f"Constancia {self.id}"
    
    class Meta:
        verbose_name = "Constancia de inscripción al programa individual"
        verbose_name_plural = "Constancias de inscripción al programa individual"

# COLEGIO_PROFESORES_POSGRADO
class ColegioProfesoresPosgrado(models.Model):
    unidad_colegio_profesores = models.CharField(max_length=255)
    nombre_sesion = models.CharField(max_length=255,null=True,blank=True)
    numero_sesion = models.IntegerField(null=True,blank=True)
    fecha_sesion = models.DateField(default=None,null=True,blank=True)

    def __str__(self):
        return self.nombre_sesion + " No. " + self.numero_sesion


# ACTA_REGISTRO_TEMA_TESIS
class ActaRegistroTemaTesis(models.Model):
    datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
    datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
    colegio_profesores = models.ForeignKey(ColegioProfesoresPosgrado, on_delete=models.CASCADE,default=None,null=True,blank=True)
    fecha = models.DateField(default=None,null=True)
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
        verbose_name = "Acta de Revision de tesis"
        verbose_name_plural = "Actas de Revision de tesis"

# PROGRAMA_ACTIVIDADES
class ProgramaActividades(models.Model):
    PERIODO_CHOICE = [
        ('A', 'A'),
        ('B', 'B'),
    ]
    
    clave = models.CharField(max_length=50)
    unidad_aprendizaje = models.CharField(max_length=100)
    creditos = models.FloatField()
    periodo = models.CharField(max_length=1,choices=PERIODO_CHOICE)
    lugar_realizacion = models.CharField(max_length=255)
    
    def __str__(self):
        return self.clave

# CONSTANCIA_PROGRAMA
class ConstanciaPrograma(models.Model):
    id_constancia_programa_individual = models.ForeignKey(ConstanciaProgramaIndividual,on_delete=models.CASCADE)
    id_programa_actividades = models.ForeignKey(ProgramaActividades,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
    
#CALENDARIO
class Calendario(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField(blank=True,null=True)
    fecha_final = models.DateTimeField(blank=True,null=True)
    class Meta:
        verbose_name = "Calendario"
        verbose_name_plural = "Calendarios"
    def __str__(self):
        return self.nombre