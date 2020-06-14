"""examen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from views.HomeView import HomeView
from models.Alumno.views import FormularioAlumnoView
from models.Candidato.views import FormularioCandidatoView
from models.Grado.views import FormularioGradoView
from models.Seccion.views import FormularioSeccionView

urlpatterns = [
    #path('admin/', admin.site.urls),
path('', HomeView.home, name='home'),
path('pagina1/', HomeView.pagina1, name='pagina1'),
path('registrarAlumno/', FormularioAlumnoView.index, name='registrarAlumno'),
path('guardarAlumno/', FormularioAlumnoView.procesar_formulario, name='guardarAlumno'),
path('registrarCandidato/', FormularioCandidatoView.index, name='registrarCandidato'),
path('guardarCandidato/', FormularioCandidatoView.procesar_formulario1, name='guardarCandidato'),
path('MostrarAlumno/', FormularioAlumnoView.lista, name="MostrarAlumno"),
path('MostrarCandidato/', FormularioCandidatoView.lista, name="MostrarCandidato"),
path('registrarGrado/', FormularioGradoView.index, name='registrarGrado'),
path('guardarGrado/', FormularioGradoView.procesar_formulario2, name='guardarGrado'),
path('MostrarGrado/', FormularioGradoView.lista, name="MostrarGrado"),
path('registrarSeccion/', FormularioSeccionView.index, name='registrarSeccion'),
path('guardarSeccion/', FormularioSeccionView.procesar_formulario3, name='guardarSeccion'),
path('MostrarSeccion/', FormularioSeccionView.lista, name="MostrarSeccion"),
]
