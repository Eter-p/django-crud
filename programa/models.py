from django.db import models
from django.contrib.auth.models import User
from formularios.models import SolicitudInscripcion,SolicitudReinscripcion,ConstanciaProgramaIndividual

# UNIDAD_DE_APRENDIZAJE
class UnidadAprendizaje(models.Model):
    clave = models.CharField(max_length=7)
    unidad_aprendizaje = models.CharField(max_length=100)
    creditos = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.unidad_aprendizaje
    class Meta:
        verbose_name = "Unidad de aprendizaje"
        verbose_name_plural = "Unidades de aprendizaje"

# PROGRAMA_SEMESTRAL
class ProgramaSemestral(models.Model):
    unidad_aprendizaje = models.ForeignKey(UnidadAprendizaje, on_delete=models.CASCADE,blank=True,null=True)
    profesor = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)
    lugar_realizacion = models.CharField(max_length=255,default="ESCOM")

    def __str__(self):
        return f"{self.unidad_aprendizaje.unidad_aprendizaje} - {self.profesor.first_name} {self.profesor.last_name}"
    class Meta:
        verbose_name = "Unidad de aprendizaje"
        verbose_name_plural = "PROGRAMA SEMESTRAL"

# INSCRIPCION_PROGRAMA
class InscripcionPrograma(models.Model):
    id_solicitud_inscripcion = models.ForeignKey(SolicitudInscripcion,on_delete=models.CASCADE)
    id_programa_semestral = models.ForeignKey(ProgramaSemestral,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_solicitud_inscripcion} - {self.id_programa_semestral.unidad_aprendizaje}"
    
    class Meta:
        verbose_name = "Relación Solicitud de incripción - Programa"
        verbose_name_plural = "Tabla Solicitudes de incripción - Programa"

# REINSCRIPCION_PROGRAMA
class ReinscripcionPrograma(models.Model):
    id_solicitud_reinscripcion = models.ForeignKey(SolicitudReinscripcion,on_delete=models.CASCADE)
    id_programa_semestral = models.ForeignKey(ProgramaSemestral,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_solicitud_reinscripcion} - {self.id_programa_semestral.unidad_aprendizaje}"
    
    class Meta:
        verbose_name = "Relación Solicitud de reincripción - Programa"
        verbose_name_plural = "Tabla Solicitudes de reincripción - Programa"
    
# CONSTANCIA_PROGRAMA
class ConstanciaPrograma(models.Model):
    id_constancia_programa_individual = models.ForeignKey(ConstanciaProgramaIndividual,on_delete=models.CASCADE)
    id_programa_actividades = models.ForeignKey(ProgramaSemestral,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"