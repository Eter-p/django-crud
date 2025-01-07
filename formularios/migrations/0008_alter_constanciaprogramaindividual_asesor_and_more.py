# Generated by Django 5.1.3 on 2025-01-06 22:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0007_alter_actaregistrotematesis_datos_academicos_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='constanciaprogramaindividual',
            name='asesor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profesor_asesor_programa_individual', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='DatosAsesor',
        ),
    ]