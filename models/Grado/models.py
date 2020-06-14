from django.db import models

class Grado(models.Model):
    nivel_academico = models.CharField(max_length=25)
    grado = models.CharField(max_length=25)
    jornada = models.CharField(max_length=20)
    codigo = models.IntegerField()

