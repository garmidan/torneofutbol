# Generated by Django 3.1 on 2020-08-24 18:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vistasymodelos', '0009_auto_20200824_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partidos',
            name='identificador',
        ),
        migrations.AddField(
            model_name='partidos',
            name='id',
            field=models.AutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]