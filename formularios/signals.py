from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import SolicitudInscripcion, InscripcionAntecedentes, AntecedentesAcademicos

@receiver(post_delete, sender=SolicitudInscripcion)
def borrar_contenidos_relacionados(sender, instance, **kwargs):
    instancias_sa = InscripcionAntecedentes.objects.filter(id_solicitud_inscripcion=instance)
    id_sa_relacionados = [sa.id_antecedentes.id for sa in instancias_sa]
    AntecedentesAcademicos.objects.filter(id__in=id_sa_relacionados).delete()
