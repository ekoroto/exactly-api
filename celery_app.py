import settings

from celery import Celery


app = Celery(
    __name__,
    config_source=settings,
    include=['apps.image.tasks',],
)

app.conf.timezone = 'UTC'
