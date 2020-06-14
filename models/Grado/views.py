from django.shortcuts import render
from django.http import HttpRequest
from models.Grado.models import Grado
from models.Grado.forms import FormularioGrado



class FormularioGradoView(HttpRequest):
    def index(request):
        grado1 = FormularioGrado()
        return render(request, "GradoIndex.html", {"form":grado1})

    def procesar_formulario2(request):
        grado1 = FormularioGrado(request.POST)
        if grado1.is_valid():
            grado1.save()
            grado1 = FormularioGrado()
        return render(request, "GradoIndex.html", {"form": grado1, "mensaje": "OK"})

    def lista(request):
        grado1 = Grado.objects.all()
        return render(request, "MostrarGrado.html", {'grado1s': grado1})



