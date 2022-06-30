import json
from collections import UserDict

from celery import Celery

uri = 'redis://localhost:6379/7'
app = Celery('tasks', backend='redis://localhost:6379/2', broker=uri)
app.conf.enable_utc = True

from time import sleep

@app.task(bind=True)
def demo2(self, a):
    print(a)
