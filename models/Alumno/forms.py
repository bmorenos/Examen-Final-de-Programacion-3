from django import forms
from models.Alumno.models import Alumno
from models.Candidato.models import Candidato

class FormularioAlumno(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'
        widgets = {'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})}

