from django.urls import path
from television import views


urlpatterns = [
    path('', views.index, name='index'),
    path('series/', views.metodoSeries, name='series'),
    path('personajes/', views.metodoPersonajes, name='pesonajes'),
    path('modificarpersonaje/', views.modificarPersonaje, name='modificarpesonaje'),
    path('updatepersonserie/', views.updatePersonSerie, name='updatepersonserie'),
]
