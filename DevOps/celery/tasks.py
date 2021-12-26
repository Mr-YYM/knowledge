from celery import Celery
import time

app = Celery('tasks', backend='rpc://', broker='amqp://localhost')

@app.task
def add(x, y, delay):
    time.sleep(delay)
    return x + y
