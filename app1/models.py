from django.db import models
# from django.contrib.auth.models import User

# # TIPOS_SOLICITUDES
# class TipoSolicitud(models.Model):
#     tipo_solicitud = models.CharField(max_length=255)

#     def __str__(self):
#         return self.tipo_solicitud

# # SOLICITUD
# class Solicitud(models.Model):
#     tipo_solicitud = models.ForeignKey(TipoSolicitud, on_delete=models.CASCADE)
#     contenido_solicitud = models.TextField()

#     def __str__(self):
#         return f"Solicitud {self.id}"

# # DATOS_PERSONALES_ALUMNO
# class DatosPersonalesAlumno(models.Model):
#     apellido_paterno = models.CharField(max_length=100)
#     apellido_materno = models.CharField(max_length=100)
#     nombre = models.CharField(max_length=100)
#     domicilio = models.CharField(max_length=255)
#     telefono_casa = models.CharField(max_length=20)
#     telefono_movil = models.CharField(max_length=20)
#     sexo = models.CharField(max_length=10)
#     correo_1 = models.EmailField()
#     correo_2 = models.EmailField(blank=True, null=True)
#     firma_alumno = models.BooleanField()

#     def __str__(self):
#         return f"{self.nombre} {self.apellido_paterno}"

# # DATOS_ACADEMICOS_ALUMNO
# class DatosAcademicosAlumno(models.Model):
#     STATUS_CHOICE = [
#         ('C', 'Tiempo Completo'),
#         ('P', 'Tiempo Parcial'),
#         ('O', 'Otro'),
#     ]
#     boleta = models.CharField(max_length=50)
#     unidad_academica_actual = models.CharField(max_length=100)
#     nom_programa_actual = models.CharField(max_length=100)
#     estatus = models.CharField(max_length=1, choices=STATUS_CHOICE, default='O')

#     def __str__(self):
#         return self.boleta

# # ANTECEDENTES_ACADEMICOS
# class AntecedentesAcademicos(models.Model):
#     nivel_academico_cursado = models.CharField(max_length=100)
#     programa_academico_cursado = models.CharField(max_length=100)
#     institucion_donde_curso = models.CharField(max_length=255)
#     estado_institucion = models.CharField(max_length=100)
#     fecha_graduacion = models.DateField()

#     def __str__(self):
#         return self.programa_academico_cursado

# # PROGRAMA_SEMESTRAL
# class ProgramaSemestral(models.Model):
#     clave = models.CharField(max_length=50)
#     unidad_aprendizaje = models.CharField(max_length=100)
#     profesor = models.CharField(max_length=100)
#     lugar_realizacion = models.CharField(max_length=255)

#     def __str__(self):
#         return self.clave

# # SOLICITUD_INSCRIPCION
# class SolicitudInscripcion(models.Model):
#     datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
#     datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
#     antecedentes = models.ForeignKey(AntecedentesAcademicos, on_delete=models.CASCADE)
#     programa_semestral = models.ForeignKey(ProgramaSemestral, on_delete=models.CASCADE)
#     firma_alumno = models.BooleanField()
#     firma_asesor = models.BooleanField()
#     firma_jefe = models.BooleanField()
#     aviso_privacidad = models.BooleanField()

#     def __str__(self):
#         return f"Solicitud Inscripción {self.id}"

# # SOLICITUD_REINSCRIPCION
# class SolicitudReinscripcion(models.Model):
#     datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
#     datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
#     programa_semestral = models.ForeignKey(ProgramaSemestral, on_delete=models.CASCADE)
#     fecha = models.DateField()
#     nom_programa_a_cursar = models.CharField(max_length=100)
#     unidad_academica_a_cursar = models.CharField(max_length=100)
#     periodo = models.CharField(max_length=50)
#     semestre_a_cursar = models.CharField(max_length=10)
#     requiere_unidad = models.BooleanField()
#     firma_alumno = models.BooleanField()
#     firma_asesor = models.BooleanField()
#     firma_jefe = models.BooleanField()

#     def __str__(self):
#         return f"Solicitud Reinscripción {self.id}"

# # DATOS_ASESOR
# class DatosAsesor(models.Model):
#     apellido_paterno = models.CharField(max_length=100)
#     apellido_materno = models.CharField(max_length=100)
#     nombre = models.CharField(max_length=100)
#     firma_asesor = models.BooleanField()

#     def __str__(self):
#         return f"{self.nombre} {self.apellido_paterno}"

# # CONSTANCIA_PROGRAMA_INDIVIDUAL
# class ConstanciaProgramaIndividual(models.Model):
#     datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
#     asesor = models.ForeignKey(DatosAsesor, on_delete=models.CASCADE)
#     programa_semestral = models.ForeignKey(ProgramaSemestral, on_delete=models.CASCADE)
#     firma_alumno = models.BooleanField()
#     firma_asesor = models.BooleanField()
#     firma_jefe = models.BooleanField()

#     def __str__(self):
#         return f"Constancia {self.id}"

# # ACTA_REGISTRO_TEMA_TESIS
# class ActaRegistroTemaTesis(models.Model):
#     datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
#     datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
#     tema_tesis = models.CharField(max_length=255)
#     objetivo_general_tesis = models.TextField()
#     nombre_director_1 = models.CharField(max_length=100)
#     nombre_director_2 = models.CharField(max_length=100, blank=True, null=True)
#     aplicacion_director = models.BooleanField()
#     base_tesis = models.TextField()
#     firma_director_1 = models.BooleanField()
#     firma_director_2 = models.BooleanField(blank=True, null=True)
#     firma_alumno = models.BooleanField()
#     firma_presidente_colegio = models.BooleanField()

#     def __str__(self):
#         return self.tema_tesis

# # ACTA_REVISION_TESIS
# class ActaRevisionTesis(models.Model):
#     datos_personales = models.ForeignKey(DatosPersonalesAlumno, on_delete=models.CASCADE)
#     datos_academicos = models.ForeignKey(DatosAcademicosAlumno, on_delete=models.CASCADE)
#     titulo_tesis = models.CharField(max_length=255)
#     porcentaje_plagio = models.FloatField()
#     conclusion_plagio = models.TextField()
#     justificacion_conclusion = models.TextField()
#     manifiesto_comision = models.TextField()
#     firma_comision_1 = models.BooleanField()
#     firma_comision_2 = models.BooleanField()
#     firma_comision_3 = models.BooleanField()
#     firma_presidente_colegio = models.BooleanField()

#     def __str__(self):
#         return self.titulo_tesis

# # COLEGIO_PROFESORES_POSGRADO
# class ColegioProfesoresPosgrado(models.Model):
#     unidad_colegio_profesores = models.CharField(max_length=255)
#     nombre_sesion = models.CharField(max_length=255)
#     numero_sesion = models.IntegerField()

#     def __str__(self):
#         return self.unidad_colegio_profesores

# # PROGRAMA_ACTIVIDADES
# class ProgramaActividades(models.Model):
#     clave = models.CharField(max_length=50)
#     unidad_aprendizaje = models.CharField(max_length=100)
#     creditos = models.FloatField()
#     periodo = models.CharField(max_length=50)
#     lugar_realizacion = models.CharField(max_length=255)
#     total_creditos = models.FloatField()
#     fecha_limite = models.DateField()

#     def __str__(self):
#         return self.clave
