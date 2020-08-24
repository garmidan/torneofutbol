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
    nombre = models.CharField(max_length=50, unique=True)
    estadio = models.ForeignKey(Estadio, on_delete=models.CASCADE)

class Partidos(models.Model):
    fecha_partido = models.CharField(max_length=50)
    visitante = models.CharField(max_length=40)
    local = models.CharField(max_length=40)
    estadio_jugaran = models.CharField(max_length=50)
    resultado_local = models.CharField(max_length=10, null=True)
    resultado_visitante = models.CharField(max_length=10, null=True)

class Posiciones(models.Model):
    puntos = models.CharField(max_length=100)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)


