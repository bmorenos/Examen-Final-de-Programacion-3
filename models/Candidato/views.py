from django.shortcuts import render
from django.http import HttpRequest
from models.Candidato.forms import FormularioCandidato
from models.Candidato.models import Candidato


class FormularioCandidatoView(HttpRequest):
    def index(request):
        candidato = FormularioCandidato()
        return render(request, "CandidatoIndex.html", {"form":candidato})

    def procesar_formulario1(request):
        candidato = FormularioCandidato(request.POST)
        if candidato.is_valid():
            candidato.save()
            candidato = FormularioCandidato()
        return render(request, "CandidatoIndex.html", {"form": candidato, "mensaje": "OK"})

    def lista(request):
        candidato = Candidato.objects.all()
        return render(request, "MostrarCandidato.html", {'candidatos': candidato})
