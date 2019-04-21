from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear', views.add_Tarea, name='crear'),
    path('lanzar', views.lanzarEvento, name='lanzar'),
    path('lanzarAr', views.lanzarArana, name='lanzarAr'),
    path('escribirTweet', views.escribirT, name='escribirTweet')
]
