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
    if 'numser' in request.GET:
        id_serie = request.GET['numser']
        personajes = servicio.getPersonajesSerie(id_serie)
        context = {
            "personajes": personajes
        }
        return render(request, 'pages/personajes.html', context)
    else:
        personajes = servicio.getPersonajes()
        context = {
            "personajes": personajes
        }
        return render(request, 'pages/personajes.html', context)


def modificarPersonaje(request):
    servicio = serviceSeries()
    if 'cajaidpersonaje' in request.POST:
        idpersonaje = request.POST['cajaidpersonaje']
        nombre = request.POST['cajanombre']
        imagen = request.POST['cajaimagen']
        idserie = request.POST['cajaserie']
        servicio.updatePersonaje(idpersonaje, nombre, imagen, idserie)
        personajes = servicio.getPersonajes()
        context = {
            "personajes": personajes
        }
        return render(request, 'pages/personajes.html?', context)
    elif 'idpersonaje' in request.GET:
        idpersonaje = request.GET['idpersonaje']
        personaje = servicio.findPersonaje(idpersonaje)
        series = servicio.getSeries()
        context = {
            "personaje": personaje,
            "series": series
        }
        return render(request, 'pages/modificarpersonaje.html', context)
    else:
        return render(request, 'pages/modificarpersonaje.html')


def updatePersonSerie(request):
    servicio = serviceSeries()
    if 'cajapersonaje' in request.POST: 
        idpers = request.POST['cajapersonaje']
        idserie = request.POST['cajaserie']
        personaje = servicio.findPersonaje(idpers)
        servicio.updatePersonaje(idpers, personaje.nombre, personaje.imagen, idserie)
        personajes = servicio.getPersonajes()
        context = {
            "personajes": personajes
        }
        return render(request, 'pages/personajes.html', context)
    else:
        series = servicio.getSeries()
        personajes = servicio.getPersonajes()
        context = {
            "series": series,
            "personajes": personajes
        }
        return render(request, 'pages/updatepersonserie.html', context)
