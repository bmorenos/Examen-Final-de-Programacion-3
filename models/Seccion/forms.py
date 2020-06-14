from django import forms

from models.Seccion.models import Secciones


class FormularioSeccion(forms.ModelForm):
    class Meta:
        model = Secciones
        fields = '__all__'
