from django.shortcuts import render
from hospitales.models import ServiceDepartamentos, ServiceHospital

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def departamentos(request):
    servicio = ServiceDepartamentos()
    departamentos = servicio.getDepartamentos()
    context = {
        "departamentos":  departamentos
    }
    return render(request, 'pages/departamentos.html', context)


def hospitales(request):
    servicio = ServiceHospital()
    hospitales = servicio.getHospitales()
    context = {
        "hospitales": hospitales
    }
    return render(request, 'pages/hospitales.html', context)


def insertardepartamento(request):
    if 'cajanum' in request.POST:
        servicio = ServiceDepartamentos()
        numero = request.POST['cajanum']
        nombre = request.POST['cajanom']
        localidad = request.POST['cajaloc']
        registro = servicio.insertDepartamento(numero, nombre, localidad)
        # mensaje = ""
        # if registro == 1:
        #     mensaje = "El nuevo departamento se ha creado correctamente."
        # elif registro == 0:
        #     mensaje = "El departamento que quiere crear ya existe en la base de datos."
        # else:
        #     mensaje = "Se ha producido un error"

        # context = {
        #     "mensaje": mensaje
        # }
        # return render(request, 'pages/insertardepartamento.html', context)
        departamentos = servicio.getDepartamentos()
        numerodept = int(request.POST['cajanum'])
        context = {
            "numerodept": numerodept,
            "departamentos": departamentos
        }
        return render(request, 'pages/departamentos.html', context)
    else:
        return render(request, 'pages/insertardepartamento.html')


def eliminardepartamento(request):
    if 'cajanum' in request.POST:
        servicio = ServiceDepartamentos()
        numero = request.POST['cajanum']
        eliminado = servicio.eliminarDepartamento(numero)
        if eliminado == 0:
            mensaje = f"El departamento {numero} no existe"
            context = {
                "mensaje": mensaje
            }
            return render(request, 'pages/eliminardepartamento.html', context)
        departamentos = servicio.getDepartamentos()
        context = {
            "departamentos": departamentos
        }
        return render(request, 'pages/departamentos.html', context)
    else:
        return render(request, 'pages/eliminardepartamento.html')
