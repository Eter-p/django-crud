# Generated by Django 5.1.1 on 2024-11-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0004_alter_datosacademicosalumno_estatus_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='actarevisiontesis',
            name='fecha',
            field=models.DateField(default=None),
        ),
        migrations.AddField(
            model_name='actarevisiontesis',
            name='firma_director_1',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='actarevisiontesis',
            name='firma_director_2',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='colegioprofesoresposgrado',
            name='fecha_sesion',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='colegioprofesoresposgrado',
            name='nombre_sesion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='colegioprofesoresposgrado',
            name='numero_sesion',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]