# Generated by Django 3.1 on 2020-08-24 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vistasymodelos', '0011_auto_20200824_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partidos',
            old_name='resul_local',
            new_name='resultado_local',
        ),
        migrations.RenameField(
            model_name='partidos',
            old_name='resul_visitante',
            new_name='resultado_visitante',
        ),
    ]