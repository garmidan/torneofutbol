# Generated by Django 3.1 on 2020-08-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vistasymodelos', '0006_auto_20200824_1147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partidos',
            name='resultado_local',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='partidos',
            name='resultado_visitante',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
