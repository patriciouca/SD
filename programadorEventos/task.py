# Celery service example: task to multiply two numbers
from __future__ import absolute_import

from __future__ import absolute_import

import os

from celery.schedules import crontab

from scraper.pedirObjeto import llamadaArana, scrapytareas
from celery.decorators import task
from celery import Celery, shared_task

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

app.conf.beat_schedule = {
    'tweet-2-hours': {
        'task': 'task.updateTwitter',
        'schedule': crontab(minute=0, hour='*/2'),
        'args':()
    },
}

app.conf.beat_schedule = {
    'mention-2-hours': {
        'task': 'task.twitter',
        'schedule': crontab(minute=0, hour='*/2'),
        'args':()
    },
}





@background(schedule=5)
def escucharTweets():
    escuchaMencion()

'''

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

'''
@task(name="updateTwitter")
def twitterStatus():
    escribirTweet()
'''







