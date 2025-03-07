from django.urls import path
from aplicacion import views

# En esta lista van a estar todas las rutas que quiero que coja la aplicación
urlpatterns = [
    path('', views.index, name='index'),
    path('viernes/', views.viernes, name='viernes'),
    path('listas/', views.listas, name='listas')
]
