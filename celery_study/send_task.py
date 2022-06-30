from celery_study.tasks import app
from celery_study.tasks import demo2
import datetime

eta = datetime.datetime.utcnow() + datetime.timedelta(seconds=2)
expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=1)
demo2.apply_async(args=['aaa'], task_id='12', eta=eta, expires=expires)

app.AsyncResult('12').revoke()
# demo2.apply_async(args=['bbb'], countdown=5, task_id='12')
