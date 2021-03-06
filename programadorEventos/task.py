# Celery service example: task to multiply two numbers
from __future__ import absolute_import

from __future__ import absolute_import
from celery.signals import worker_process_init
from multiprocessing import current_process
import os

from celery.schedules import crontab
from django.conf import settings

from graficas.graficas import generarGrafica
from scraper.dropbox import listarArchivos
from scraper.pedirObjeto import llamadaArana, scrapytareas, scrapytodaslastareas

from celery.decorators import task
from celery import Celery, shared_task


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled1.settings')

app = Celery('tasks', broker='amqp://guest@localhost//',  backend='djcelery.backends.database:DatabaseBackend')
app.config_from_object('django.conf:settings', namespace='CELERY')

@shared_task
def scrapearTareas():
    import billiard as multiprocessing
    scrapytodaslastareas()

@shared_task
def multiply(a, b):
    return a * b

@shared_task
def sc():
    llamadaArana()
    return "ok"

@shared_task
def twitterStatus():
    generarGrafica()
    listarArchivos()







