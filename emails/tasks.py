from celery import shared_task
from django.core.mail import send_mass_mail
from email_automator import settings
from .models import ScheduledEmail


@shared_task(bind=True)
def send_email_newsletter(self):
    scheduled_email = ScheduledEmail.objects.filter(sent_status=False).first()
    if scheduled_email:
        print("003")
        emails = scheduled_email.curate_emails()
        try:
            send_mass_mail(
                emails,
                fail_silently=False,
                )
            scheduled_email.mark_as_sent()
        except Exception as e:
            print(f"Email sending failed: {str(e)}")     
    return "No scheduled emails"

    