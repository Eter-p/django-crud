# Generated by Django 5.1.3 on 2024-11-29 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formularios', '0006_calendario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datospersonalesalumno',
            old_name='sexo',
            new_name='genero',
        ),
    ]
