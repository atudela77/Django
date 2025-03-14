from django.urls import path, include
from hospitales import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departamentos/', views.departamentos, name='departamentos'),
    # El siguiente es el mío #
    path('departamentosatm/', views.departamentosatm, name='departamentosatm'),
    path('hospitales/', views.hospitales, name='hospitales'),
    path('insertardepartamento/', views.insertardepartamento, name='insertardepartamento'),
    path('eliminardepartamento/', views.eliminardepartamento, name='eliminardepartamento'),
    path('modificardepartamento/', views.modificarDepartamento, name='modificardepartamento'),
    path('detallesdepartamento/', views.detallesDepartamento, name='detallesdepartamento'),
    path('empleadosdepartamento/', views.empleadosdepartamento, name='empleadosdepartamento'),
]
