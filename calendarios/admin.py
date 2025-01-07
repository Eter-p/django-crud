from django.contrib import admin

# Register your models here.
from .models import *

class CalendarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha_inicio', 'fecha_final')

admin.site.register(Calendario,CalendarioAdmin)
