
from celery import chain
from django.shortcuts import render
import io

# Create your views here.
from django.http import HttpResponse
from django.utils import timezone


from graficas.graficas import generarGrafica
from lanzamientoTareas.models import TareaForm, Tarea
from programadorEventos.task import multiply
from scraper.dropbox import SubirDropbox, DescargarDropbox
from scraper.pedirObjeto import llamadaArana, scrapytareas
from twitter.twitter import escribirTweet,escuchaMencion
from programadorEventos.task import scrapearTareas


def index(request):
    return render(request, 'lanzamientoTareas/index.html', {'tareas':Tarea.objects.all()})

def add_Tarea(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            tarea = form.save(commit=False)
            tarea.fecha = timezone.now()
            tarea.save()
            return render(request, 'lanzamientoTareas/index.html',{'tareas':Tarea.objects.all()})

    else:
        form = TareaForm
    return render(request, 'lanzamientoTareas/edit_tarea.html', {'form': form})


def lanzarEvento(request):
    duplicate = multiply.s(2)
    task = chain(multiply.s(4, 5), multiply.s(2))
    promise = task.delay()
    return HttpResponse(promise.get())

def lanzarArana(request):
    scrapytareas()
    return HttpResponse("ok")

def escribirT(request):
    escribirTweet()
    return HttpResponse("ok")

def escucharT(request):
    escuchaMencion()

    return HttpResponse("ok")

def grafica(request):
    generarGrafica()
    return HttpResponse("ok")

def getTareas(request):
    scrapearTareas()
    return "a"

def dropbox(request):
    DescargarDropbox('/datos/Beuya Muje.csv')
    return "a"