from django.db import models
from subscribers.models import Subscriber
from django.urls import reverse
from email_automator import settings

class ScheduledEmail(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    scheduled_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    sent_status = models.BooleanField(default=False)

    def __str__(self):
        return self.subject[:20]

    def get_absolute_url(self): # new
        return reverse("email_scheduled", args=[str(self.id)])

    def mark_as_sent(self):
        self.sent_status = True
        self.save()

    def curate_emails(self, subscribers=Subscriber.objects.all()):
        emails = []

        for subscriber in subscribers:
            email = (
                self.subject,
                self.message,
                settings.EMAIL_HOST_USER,
                [subscriber.email],
            )
            emails.append(email)

        return emails