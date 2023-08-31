from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.name