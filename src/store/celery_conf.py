import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.settings")

app = Celery("store")

app.conf.task_serializer = "pickle"
app.conf.event_serializer = "pickle"

app.conf.result_serializer = "pickle"
app.conf.accept_content = [
    "application/json",
    "application/x-python-serialize",
]
app.conf.result_accept_content = [
    "application/json",
    "application/x-python-serialize",
]

app.config_from_object("django.conf:settings", namespace="CELERY")


# Load task modules from all registered Django apps.
app.autodiscover_tasks()
