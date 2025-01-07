# Generated by Django 5.1.3 on 2025-01-02 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('fecha_inicio', models.DateTimeField(blank=True, null=True)),
                ('fecha_final', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Calendario',
                'verbose_name_plural': 'Calendarios',
            },
        ),
    ]