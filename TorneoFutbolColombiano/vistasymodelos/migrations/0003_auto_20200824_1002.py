# Generated by Django 3.1 on 2020-08-24 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vistasymodelos', '0002_partidos'),
    ]

    operations = [
        migrations.AddField(
            model_name='partidos',
            name='estadio_jugaran',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
