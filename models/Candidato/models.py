from django.db import models

class Candidato(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    profesion = models.CharField(max_length=20)
    universidad = models.CharField(max_length=25)
    puesto = models.CharField(max_length=20)
    codigo = models.IntegerField()
