from django.shortcuts import render
from television.models import serviceSeries


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def metodoSeries(request):
    servicio = serviceSeries()
    series = servicio.getSeries()
    context = {
        "series": series
    }
    return render(request, 'pages/series.html', context)


def metodoPersonajes(request):
    servicio = serviceSeries()
    personajes = servicio.getPersonajes()
    context = {
        "personajes": personajes
    }
    return render(request, 'pages/personajes.html', context)
