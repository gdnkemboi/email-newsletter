from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse

from .forms import SubscribeForm
from .tasks import send_notification_mail

class SubscribeView(CreateView):
    form_class = SubscribeForm
    template_name = "subscribers/subscribe.html"
    success_url = reverse_lazy("subscribed")

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data["email"]
        send_notification_mail.delay(email)
        return response

class SubscribedView(TemplateView):
    template_name = "subscribers/subscribed.html"
