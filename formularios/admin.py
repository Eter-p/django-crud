from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Calendario)
admin.site.register(SolicitudInscripcion)
admin.site.register(SolicitudReinscripcion)
admin.site.register(ConstanciaProgramaIndividual)
admin.site.register(ActaRegistroTemaTesis)
admin.site.register(ActaRevisionTesis)