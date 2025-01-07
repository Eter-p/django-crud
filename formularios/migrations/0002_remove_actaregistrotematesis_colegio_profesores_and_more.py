# Generated by Django 5.1.3 on 2025-01-04 01:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actaregistrotematesis',
            name='colegio_profesores',
        ),
        migrations.AddField(
            model_name='actaregistrotematesis',
            name='fecha_sesion',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='actaregistrotematesis',
            name='nombre_sesion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='actaregistrotematesis',
            name='numero_sesion',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='actaregistrotematesis',
            name='unidad_colegio_profesores',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='solicitudinscripcion',
            name='asesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profesor_asesor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='solicitudinscripcion',
            name='jefe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profesor_jefe', to=settings.AUTH_USER_MODEL),
        ),
    ]