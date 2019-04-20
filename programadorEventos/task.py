# Celery service example: task to multiply two numbers
from __future__ import absolute_import

from __future__ import absolute_import

import os
from scraper.pedirObjeto import llamadaArana

from celery import Celery, shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'untitled1.settings')

# Redis
app = Celery('tasks', broker='amqp://guest@localhost//',  backend='redis://localhost:6379/0')


@shared_task
def multiply(a, b):
    return a * b

@shared_task
def sc():
    llamadaArana()
    return "ok"
