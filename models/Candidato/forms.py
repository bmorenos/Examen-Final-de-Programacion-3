from django import forms
from models.Candidato.models import Candidato


class FormularioCandidato(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = '__all__'
