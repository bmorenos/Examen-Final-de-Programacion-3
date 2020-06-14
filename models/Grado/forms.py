from django import forms

from models.Grado.models import Grado


class FormularioGrado(forms.ModelForm):
    class Meta:
        model = Grado
        fields = '__all__'
