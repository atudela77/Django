from django.urls import path, include
from hospitales import views

urlpatterns = [
    path('', views.index, name='index'),
    path('departamentos/', views.departamentos, name='departamentos'),
    path('hospitales/', views.hospitales, name='hospitales'),
    path('insertardepartamento/', views.insertardepartamento, name='insertardepartamento'),
    path('eliminardepartamento/', views.eliminardepartamento, name='eliminardepartamento'),
]
