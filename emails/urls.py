from django.urls import path
from .views import ScheduleEmailView, EmailScheduledView, EmailsView

urlpatterns = [
    path("", EmailsView.as_view(), name="emails_list"),
    path("schedule-email/", ScheduleEmailView.as_view(), name="schedule_email"),
    path("scheduled-email/<int:pk>/", EmailScheduledView.as_view(), name="email_scheduled"),
]