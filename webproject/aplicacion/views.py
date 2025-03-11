from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("¡¡Mi primera página Django!!")
    return render(request, 'aplicacion/index.html')


def viernes(request):
    return render(request, 'aplicacion/viernes.html')


def listas(request):
    return render(request, 'aplicacion/listas.html')


def peliculas(request):
    return render(request, 'aplicacion/peliculas.html')
