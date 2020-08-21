from django.db import models

# Creacion de modelos

class Rol(models.Model):
    nombre = models.CharField(max_length=30)

class Usuario(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    cedula = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    clave = models.CharField(max_length=20)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

class Estadio(models.Model):
    nombre = models.CharField(max_length=50)    

class Equipo(models.Model):
    nombre = models.CharField(max_length=50)
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)

class Partidos(models.Model):
    nombres_equipos = models.CharField(max_length=100)
    fecha_partido = models.CharField(max_length=50)
    visitante = models.CharField(max_length=40)
    local = models.CharField(max_length=40)


