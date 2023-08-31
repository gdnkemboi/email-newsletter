from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from subscribers.models import Subscriber
from django.utils import timezone
from django.urls import reverse

class ScheduledEmail(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    subs = models.ManyToManyField(Subscriber, blank=True)
    scheduled_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    sent_status = models.BooleanField(default=False)

    def __str__(self):
        return self.subject[:20]

    def get_absolute_url(self): # new
        return reverse("email_scheduled", args=[str(self.id)])

@receiver(pre_save, sender=ScheduledEmail)
def update_sent_status(sender, instance, **kwargs):
    if instance.scheduled_time and instance.scheduled_time < timezone.now():
        instance.sent_status = True
    else:
        instance.sent_status = False