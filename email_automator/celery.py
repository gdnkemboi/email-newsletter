import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "email_automator.settings")

app = Celery("email_automator")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

app.conf.enable_utc = False

app.conf.update(timezone="Africa/Nairobi")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "send-email-newsletter": {
        "task": "emails.tasks.send_email_newsletter",
        "schedule": crontab(
            hour=13, minute=25
        ),  # crontab(hour=6, minute=0, day_of_week=1),
    },
}
