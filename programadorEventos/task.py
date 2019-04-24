# Celery service example: task to multiply two numbers
from __future__ import absolute_import

from __future__ import absolute_import

import os
from scraper.pedirObjeto import llamadaArana

from celery import Celery, shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled1.settings')

app = Celery('tasks', broker='amqp://guest@localhost//',  backend='redis://localhost:6379/0')

'''
app.conf.beat_schedule = {
    'add-every-3-hours': {
        'task': 'tasks.add',
        'schedule': crontab(minute=0, hour='*/3'),
        'args': ()
    },
}

app.conf.timezone = 'Europe/Madrid'
'''
@shared_task
def multiply(a, b):
    return a * b

@shared_task
def sc():
    llamadaArana()
    return "ok"
