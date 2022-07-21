import json
from collections import UserDict

from celery import Celery, Task
from celery.worker.request import Request

uri = 'redis://localhost:6379/7'
app = Celery('tasks', backend='redis://localhost:6379/2', broker=uri)
app.conf.enable_utc = True
import time


class MyRequset(Request):
    def on_timeout(self, soft, timeout):
        print(self.args)

    def on_failure(self, exc_info, send_failed_event=True, return_ok=False):
        return None


class MyTask(Task):
    Request = MyRequset

    def run(self, a, b):
        time.sleep(3)
        print(a + b)


add = app.register_task(MyTask())
