from django.http import HttpResponse
from django.template.loader import get_template


class HomeView():
    def home(self):
        plantilla = get_template('index.html')
        return HttpResponse(plantilla.render())

    def pagina1(self):
        return HttpResponse('hola desde una nueva ruta')


