from django.db import models

class Calendario(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateTimeField(blank=True,null=True)
    fecha_final = models.DateTimeField(blank=True,null=True)
    class Meta:
        verbose_name = "Calendario"
        verbose_name_plural = "Calendarios"
    def __str__(self):
        return self.nombre