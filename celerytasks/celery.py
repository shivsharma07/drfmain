from __future__ import absolute_import, unicode_literals
from celery import Celery

# app = Celery('celerytasks',
#              broker='amqp://',
#              backend='amqp://',
#              include=['celerytasks.tasks'])

app = Celery('celerytasks', backend='redis://localhost', broker='pyamqp://')


# Optional configuration
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()
