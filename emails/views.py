from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from django.db.models import Count
from .forms import ScheduleEmailForm
from .models import ScheduledEmail
from subscribers.models import Subscriber
from django.db.models import Count, Q, F

class ScheduleEmailView(CreateView):
    form_class = ScheduleEmailForm
    template_name = "emails/schedule_email.html"

class EmailScheduledView(DetailView):
    model = ScheduledEmail
    template_name = "emails/email_scheduled.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        scheduled_email = self.object  # Get the current instance of ScheduledEmail
        subscribers = Subscriber.objects.filter(date_subscribed__lte=scheduled_email.scheduled_time)
        context['subscribers'] = subscribers
        context['subscriber_count'] = subscribers.count()
        return context

class EmailsView(ListView):
    model = ScheduledEmail
    template_name = "emails/emails_list.html"