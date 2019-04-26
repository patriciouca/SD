# Celery service example: task to multiply two numbers
from __future__ import absolute_import

from __future__ import absolute_import

import os

from celery.schedules import crontab

from scraper.pedirObjeto import llamadaArana, scrapytareas
from celery.decorators import task
from celery import Celery, shared_task
from twitter.twitter import escuchaMencion

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled1.settings')

app = Celery('tasks', broker='amqp://guest@localhost//',  backend='redis://localhost:6379/0')

'''
app.conf.beat_schedule = {
    'scrappi-every-3-hours': {
        'task': 'tasks.tareas',
        'schedule': crontab(minute=0, hour='*/3'),
        'args': ()
    },
}
app.conf.timezone = 'Europe/Madrid'
'''


@task(name="twitter")
def escucharTweets():
    escuchaMencion()


@task(name="tareas")
def scrapearTareas():
    scrapytareas()

@shared_task
def multiply(a, b):
    return a * b

@shared_task
def sc():
    llamadaArana()
    return "ok"
