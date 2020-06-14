from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    codigo = models.IntegerField()