# Celery service example: task to multiply two numbers
from __future__ import absolute_import

from __future__ import absolute_import
from celery.signals import worker_process_init
from multiprocessing import current_process
import os

from celery.schedules import crontab

from scraper.pedirObjeto import llamadaArana, scrapytareas
from celery.decorators import task
from celery import Celery, shared_task



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled1.settings')

app = Celery('tasks', broker='amqp://guest@localhost//',  backend='redis://localhost:6379/0')

@worker_process_init.connect
def fix_multiprocessing(**kwargs):
    try:
        current_process()._config
    except AttributeError:
        current_process()._config = {'semprefix': '/mp'}

@shared_task
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







