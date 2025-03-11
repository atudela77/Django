from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'informacion/index.html')


def pelis(request):
    return render(request, 'informacion/pelis.html')


def futbol(request):
    nombre = "Real Madrid"
    data = {
        "equipo": nombre
    }
    return render(request, 'informacion/futbol.html', data)


def jugadores(request):
    listaJugadores = [
        {
            "Nombre": "Cristiano Ronaldo",
            "Demarcacion": "Delantero",
            "Numero": 7
        },
        {
            "Nombre": "Guti",
            "Demarcacion": "Centrocampista",
            "Numero": 14
        },
        {
            "Nombre": "Karim Benzema",
            "Demarcacion": "Delantero",
            "Numero": 9
        },
        {
            "Nombre": "Toni Kroos",
            "Demarcacion": "Centrocampista",
            "Numero": 8
        },
        {
            "Nombre": "Thibaut Courtois",
            "Demarcacion": "Portero",
            "Numero": 1
        }
    ]
    context = {
        'jugadores': listaJugadores
    }
    return render(request, 'informacion/jugadores.html', context)


def colores(request):
    # Recuperamos la variable que nos envían mediante GET
    if ('micolor' in request.GET):
        colorRecibido = request.GET['micolor']
        # Con el color recibido lo devolvemos al dibujo para pintarlo
        context = {
            "colordibujo": colorRecibido
        }
        return render(request, 'informacion/colores.html', context)
    else:
        return render(request, 'informacion/colores.html')


def saludo(request):
    # Se recupera la variable enviada por POST desde el
    #   formulario >> name="cajanombre"
    if ('cajanombre' in request.POST):
        nombreRecibido = request.POST['cajanombre']
        context = {
            "nombre": nombreRecibido
        } 
        return render(request, 'informacion/saludo.html', context)
    else:
        return render(request, 'informacion/saludo.html')


def sumarnumeros(request):
    if 'cajanumero1' in request.POST:
        num1 = request.POST['cajanumero1']
        num2 = request.POST['cajanumero2']
        suma = int(num1) + int(num2)
        context = {
            "suma": suma,
            "numero1": num1,
            "numero2": num2
        }
        return render(request, 'informacion/sumarnumeros.html', context)
    else:
        return render(request, 'informacion/sumarnumeros.html')
