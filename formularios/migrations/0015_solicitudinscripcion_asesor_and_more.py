# Generated by Django 5.1.3 on 2024-12-09 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0014_alter_programasemestral_clave_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudinscripcion',
            name='asesor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='solicitudinscripcion',
            name='jefe',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
