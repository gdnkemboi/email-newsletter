from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import SubscribeForm

class SubscribeView(CreateView):
    form_class = SubscribeForm
    template_name = "subscribers/subscribe.html"
    success_url = reverse_lazy("subscribed")

class SubscribedView(TemplateView):
    template_name = "subscribers/subscribed.html"
