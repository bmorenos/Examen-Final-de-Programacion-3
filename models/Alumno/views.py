from django.shortcuts import render
from django.http import HttpRequest
from models.Alumno.forms import FormularioAlumno
from models.Alumno.models import Alumno


class FormularioAlumnoView(HttpRequest):
    def index(request):
        alumno = FormularioAlumno()
        return render(request, "AlumnoIndex.html", {"form":alumno})

    def procesar_formulario(request):
        alumno = FormularioAlumno(request.POST)
        if alumno.is_valid():
            alumno.save()
            alumno = FormularioAlumno()
        return render(request, "AlumnoIndex.html", {"form": alumno, "mensaje": "ok"})

    def lista(request):
        alumno = Alumno.objects.all()
        return render(request, "MostrarAlumno.html", {'alumnos': alumno})


