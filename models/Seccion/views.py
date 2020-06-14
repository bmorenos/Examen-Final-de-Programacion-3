from django.shortcuts import render
from django.http import HttpRequest
from models.Seccion.models import Secciones
from models.Seccion.forms import FormularioSeccion

class FormularioSeccionView(HttpRequest):
    def index(request):
        seccion = FormularioSeccion()
        return render(request, "SeccionIndex.html", {"form":seccion})

    def procesar_formulario3(request):
        seccion = FormularioSeccion(request.POST)
        if seccion.is_valid():
            seccion.save()
            seccion = FormularioSeccion()
        return render(request, "SeccionIndex.html", {"form": seccion, "mensaje": "OK"})

    def lista(request):
        seccion = Secciones.objects.all()
        return render(request, "MostrarSeccion.html", {'seccions': seccion})
