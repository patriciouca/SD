from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear', views.add_Tarea, name='crear'),
    path('lanzar', views.lanzarEvento, name='lanzar'),
    path('lanzarAr', views.lanzarArana, name='lanzarAr'),
    path('escribirTweet', views.escribirT, name='escribirTweet'),
    path('generarGrafica', views.grafica, name='generarGrafica'),
    path('getTareas', views.getTareas, name='getTareas'),
    path('escuchaMencion', views.escucharT, name='escuchaMencion'),
    path('dropboxHacer', views.dropbox, name='dropboxHacer'),
    path('procScrapear', views.procesoScrapear, name='procScrapear')
]
