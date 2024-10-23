from django.db import models

# DATOS_PERSONALES_ALUMNO
class DatosPersonalesAlumno(models.Model):
    SEXO_CHOICE = [
        ('H', 'H'),
        ('M', 'M')
    ]
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=255)
    telefono_casa = models.CharField(max_length=20)
    telefono_movil = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1,choices=SEXO_CHOICE,default=None)
    correo_1 = models.EmailField()
    correo_2 = models.EmailField(blank=True, null=True)
    firma_alumno = models.BooleanField()

    def __str__(self):
        return f"{self.apellido_paterno} {self.apellido_materno} {self.nombre}"
    
# DATOS_ACADEMICOS_ALUMNO
class DatosAcademicosAlumno(models.Model):
    ESTATUS_CHOICE = [
        ('C', 'Tiempo Completo'),
        ('P', 'Tiempo Parcial'),
        ('O', 'Otro'),
    ]
    boleta = models.CharField(max_length=50)
    unidad_academica_actual = models.CharField(max_length=100)
    nom_programa_actual = models.CharField(max_length=100)
    estatus = models.CharField(max_length=1, choices=ESTATUS_CHOICE, default='C')

    def __str__(self):
        return self.boleta

# ANTECEDENTES_ACADEMICOS
class AntecedentesAcademicos(models.Model):
    NIVEL_CHOICE = [
        ('L', 'Licenciatura'),
        ('E', 'Especialidad'),
        ('M', 'Maestria'),
        ('D', 'Doctorado'),
    ]
    nivel_academico_cursado = models.CharField(max_length=1,choices=NIVEL_CHOICE,default='L')
    programa_academico_cursado = models.CharField(max_length=100)
    institucion_donde_curso = models.CharField(max_length=255)
    estado_institucion = models.CharField(max_length=100)
    fecha_graduacion = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.programa_academico_cursado

# PROGRAMA_SEMESTRAL
class ProgramaSemestral(models.Model):
    clave = models.CharField(max_length=50)
    unidad_aprendizaje = models.CharField(max_length=100)
    profesor = models.CharField(max_length=100)
    lugar_realizacion = models.CharField(max_length=255)

    def __str__(self):
        return self.clave

# SOLICITUD_INSCRIPCION
class SolicitudInscripcion(models.Model):
    datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
    datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
    firma_alumno = models.BooleanField()
    firma_asesor = models.BooleanField()
    firma_jefe = models.BooleanField()
    aviso_privacidad = models.BooleanField()

    def __str__(self):
        return f"Solicitud Inscripción {self.id}"

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
    nom_programa_a_cursar = models.CharField(max_length=100)
    unidad_academica_a_cursar = models.CharField(max_length=100)
    periodo = models.CharField(max_length=50)
    semestre_a_cursar = models.IntegerField(choices=NIVEL_CHOICE)
    requiere_unidad = models.BooleanField()
    firma_alumno = models.BooleanField()
    firma_asesor = models.BooleanField()
    firma_jefe = models.BooleanField()

    def __str__(self):
        return f"Solicitud Reinscripción {self.id}"

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
    firma_asesor = models.BooleanField()

    def __str__(self):
        return f"{self.apellido_paterno} {self.apellido_materno} {self.nombre}"

# CONSTANCIA_PROGRAMA_INDIVIDUAL
class ConstanciaProgramaIndividual(models.Model):
    datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
    asesor = models.ForeignKey(DatosAsesor, on_delete=models.CASCADE)
    firma_alumno = models.BooleanField()
    firma_asesor = models.BooleanField()
    firma_jefe = models.BooleanField()

    def __str__(self):
        return f"Constancia {self.id}"

# ACTA_REGISTRO_TEMA_TESIS
class ActaRegistroTemaTesis(models.Model):
    datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
    datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
    tema_tesis = models.CharField(max_length=255)
    objetivo_general_tesis = models.TextField()
    nombre_director_1 = models.CharField(max_length=100)
    nombre_director_2 = models.CharField(max_length=100, blank=True, null=True)
    aplicacion_director = models.BooleanField()
    base_tesis = models.TextField()
    firma_director_1 = models.BooleanField()
    firma_director_2 = models.BooleanField(blank=True, null=True)
    firma_alumno = models.BooleanField()
    firma_presidente_colegio = models.BooleanField()

    def __str__(self):
        return f"Acta de Registro de tesis {self.id}"

# ACTA_REVISION_TESIS
class ActaRevisionTesis(models.Model):
    MANIFIESTO_CHOICE = [
        ('A', 'Aprobar'),
        ('S', 'Suspender'),
        ('N', 'No Aprobar'),
    ]
    datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
    datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
    titulo_tesis = models.CharField(max_length=255)
    porcentaje_plagio = models.FloatField()
    conclusion_plagio = models.TextField()
    justificacion_conclusion = models.TextField()
    manifiesto_comision = models.TextField(max_length=1,choices=MANIFIESTO_CHOICE)
    firma_comision_1 = models.BooleanField()
    firma_comision_2 = models.BooleanField()
    firma_comision_3 = models.BooleanField()
    firma_presidente_colegio = models.BooleanField()

    def __str__(self):
        return f"Acta de Revision de tesis {self.id}"

# COLEGIO_PROFESORES_POSGRADO
class ColegioProfesoresPosgrado(models.Model):
    unidad_colegio_profesores = models.CharField(max_length=255)
    nombre_sesion = models.CharField(max_length=255)
    numero_sesion = models.IntegerField()

    def __str__(self):
        return self.nombre_sesion + " No. " + self.numero_sesion

# PROGRAMA_ACTIVIDADES
class ProgramaActividades(models.Model):
    clave = models.CharField(max_length=50)
    unidad_aprendizaje = models.CharField(max_length=100)
    creditos = models.FloatField()
    periodo = models.CharField(max_length=50)
    lugar_realizacion = models.CharField(max_length=255)
    total_creditos = models.FloatField()
    fecha_limite = models.DateField()

    def __str__(self):
        return self.clave

# CONSTANCIA_PROGRAMA
class ConstanciaPrograma(models.Model):
    id_constancia_programa_individual = models.ForeignKey(ConstanciaProgramaIndividual,on_delete=models.CASCADE)
    id_programa_actividaes = models.ForeignKey(ProgramaActividades,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"