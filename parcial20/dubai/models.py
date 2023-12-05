from django.db import models
from django.utils import timezone


class Viaje(models.Model):
    destino = models.CharField(max_length=100, default="Untitled Trip")
    descripcion = models.TextField(default=timezone.now)
    fecha_llegada = models.DateField()
    hora_llegada = models.TimeField()
    fecha_salida = models.DateField()
    hora_salida = models.TimeField()
    lugar_salida = models.CharField(max_length=100)
    lugar_llegada = models.CharField(max_length=100)
    espacios_vigentes = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.destino} - {self.lugar_salida} a {self.lugar_llegada}"


class Registro(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    edad = models.IntegerField()
    correo_electronico = models.EmailField()
    sexo = models.CharField(max_length=20)
    numero_telefono = models.CharField(max_length=10)
    destino = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"


class Reserva(models.Model):
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    edad = models.IntegerField()
    correo_electronico = models.EmailField()
    sexo = models.CharField(max_length=20)
    destino = models.CharField(max_length=200)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cantidad_adultos = models.IntegerField(default=1)
    cantidad_menores = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - {self.destino}"
