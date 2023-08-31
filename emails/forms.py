from django.forms import ModelForm, SplitDateTimeField, SplitDateTimeWidget
from .models import ScheduledEmail

class ScheduleEmailForm(ModelForm):
    scheduled_time = SplitDateTimeField(widget=SplitDateTimeWidget(date_attrs={"type": "date"}, time_attrs={"type": "time"}))
    class Meta:
        model = ScheduledEmail
        fields = ["subject", "message", "scheduled_time"] 
        