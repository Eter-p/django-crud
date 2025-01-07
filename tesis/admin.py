from django.contrib import admin
from .models import ActaRegistroTemaTesis,ActaRevisionTesis,ColegioProfesoresPosgrado

# Register your models here.
admin.site.register(ActaRegistroTemaTesis)
admin.site.register(ActaRevisionTesis)
admin.site.register(ColegioProfesoresPosgrado)
