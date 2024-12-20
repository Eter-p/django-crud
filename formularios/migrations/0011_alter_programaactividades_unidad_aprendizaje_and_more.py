# Generated by Django 5.1.3 on 2024-12-01 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0010_alter_programaactividades_unidad_aprendizaje'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programaactividades',
            name='unidad_aprendizaje',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='programasemestral',
            name='unidad_aprendizaje',
            field=models.CharField(choices=[('09B5786', 'Métodos matemáticos para el análisis de sistemas y señales'), ('09B5787', 'Fundamentos de comunicaciones móviles'), ('O1', 'Optativa I'), ('09B5789', 'Seminario I'), ('09B5791', 'Arquitectura de dispositivos móviles'), ('O2', 'Optativa II'), ('05B4670', 'Trabajo tesis'), ('09B5792', 'Seminario II'), ('O3', 'Optativa III'), ('O4', 'Optativa IV'), ('05B4670', 'Trabajo tesis'), ('09B5794', 'Seminario III'), ('13A6641', 'Seminario IV'), ('TESIS', 'Tesis')], default='el', max_length=100),
        ),
    ]
