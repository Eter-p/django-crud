# Generated by Django 5.1.3 on 2024-12-09 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0017_alter_programasemestral_clave_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programasemestral',
            name='clave',
            field=models.CharField(choices=[('09B5786', '09B5786'), ('09B5787', '09B5787'), ('000OPT1', '00000O1'), ('09B5789', '09B5789'), ('09B5791', '09B5791'), ('000OPT2', '00000O2'), ('05B4670', '05B4670'), ('09B5792', '09B5792'), ('000OPT3', '00000O3'), ('000OPT4', '00000O4'), ('05B4670', '05B4670'), ('09B5794', '09B5794'), ('13A6641', '13A6641'), ('00TESIS', '00TESIS')], max_length=7),
        ),
    ]