from celery import shared_task
from django.core.mail import send_mail
from email_automator import settings

@shared_task(bind=True)
def send_notification_mail(self, target_mail):
    mail_subject = "Welcome on Board!"
    message = "Thank You for subscribing."
    try:    
        send_mail(
            subject = mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
        recipient_list=[target_mail],
        fail_silently=False,
        )
    except Exception as e:
        print(f"Email sending failed: {str(e)}")
    return "Done"
