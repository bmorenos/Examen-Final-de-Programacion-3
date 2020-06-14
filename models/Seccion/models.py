from django.db import models

class Secciones(models.Model):
    jornada = models.CharField(max_length=25)
    seccion = models.CharField(max_length=25)
    codigo = models.IntegerField()

