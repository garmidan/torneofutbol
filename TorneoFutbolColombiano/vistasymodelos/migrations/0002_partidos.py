# Generated by Django 3.1 on 2020-08-21 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vistasymodelos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres_equipos', models.CharField(max_length=100)),
                ('fecha_partido', models.CharField(max_length=50)),
                ('visitante', models.CharField(max_length=40)),
                ('local', models.CharField(max_length=40)),
            ],
        ),
    ]