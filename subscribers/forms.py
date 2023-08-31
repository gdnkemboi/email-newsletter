from django.forms import ModelForm
from .models import Subscriber

class SubscribeForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ["email"]