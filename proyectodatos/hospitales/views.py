from django.shortcuts import render
from hospitales.models import ServiceDepartamentos, ServiceHospital, serviceEmpleados

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
    elif 'id' in request.GET:
        num = int(request.GET['id'])
        context = {"num": num}
        return render(request, 'pages/eliminardepartamento.html', context)
    else:
        return render(request, 'pages/eliminardepartamento.html')


def eliminardepartamentov2(request):
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
    elif 'id' in request.GET:
        servicio = ServiceDepartamentos()
        num = int(request.GET['id'])
        eliminado = servicio.eliminarDepartamento(num)
        departamentos = servicio.getDepartamentos()
        context = {
            "departamentos": departamentos
        }
        return render(request, 'pages/departamentos.html', context)
    else:
        return render(request, 'pages/eliminardepartamento.html')


def modificarDepartamento(request):
    servicio = ServiceDepartamentos()
    if 'cajanum' in request.POST:
        numero = request.POST['cajanum']
        nombre = request.POST['cajanom']
        localizacion = request.POST['cajaloc']
        insertado = servicio.modificarDepartamento(numero, nombre, localizacion)
        # mensaje = ""
        # if insertado == 1:
        #     mensaje = f"El departamento {numero} se ha modificado correctamente."
        # else:
        #     mensaje = f"El departamento {numero} no existe"
        # context = {
        #     "mensaje": mensaje
        # }
        # return render(request, 'pages/modificardepartamento.html', context)
        departamentos = servicio.getDepartamentos()
        numerodept = int(request.POST['cajanum'])
        context = {
            "numerodept": numerodept,
            "departamentos": departamentos
        }
        return render(request, 'pages/departamentos.html', context)
    elif 'id' in request.GET:
        num=request.GET['id']
        departamento = servicio.detallesDepartamento(num)
        context = {
            "departamento": departamento
        }
        return render(request, 'pages/modificardepartamento.html', context)
    else:
        return render(request, 'pages/modificardepartamento.html')


def departamentosatm(request):
    servicio = ServiceDepartamentos()
    departamentos = servicio.getDepartamentos()
    context = {
        "departamentos":  departamentos
    }
    return render(request, 'pages/departamentosatm.html', context)


def detallesDepartamento(request):
    if 'id' in request.GET:
        servicio = ServiceDepartamentos()
        numero = request.GET['id']
        departamento = servicio.detallesDepartamento(numero)
        context = {
            "departamento": departamento
        }
        return render(request, 'pages/detallesdepartamento.html', context)
    else:
        return render(request, 'pages/detallesdepartamento.html')


def empleadosdepartamento_v1(request):
    servicio = serviceEmpleados()
    if 'cajanum' in request.POST:
        numdept = request.POST['cajanum']
        empleados = servicio.empleadosDepartamento(numdept)
        context = {
            "numdept": numdept,
            "empleados": empleados
        }
        return render(request, 'pages/empleadosdepartamento.html', context)
    else:
        return render(request, 'pages/empleadosdepartamento.html')


def empleadosdepartamento(request):
    servicio = serviceEmpleados()
    servicioDept = ServiceDepartamentos()
    departamentos = servicioDept.getDepartamentos()
    if 'cajanum' in request.POST:
        numdept = request.POST['cajanum']
        empleados = servicio.empleadosDepartamento(numdept)
        context = {
            "numdept": numdept,
            "empleados": empleados,
            "departamentos": departamentos
        }
        return render(request, 'pages/empleadosdepartamento.html', context)
    else:
        empleados = servicio.getEmpleados()
        context = {
            "empleados": empleados,
            "departamentos": departamentos
        }
        return render(request, 'pages/empleadosdepartamento.html', context)
