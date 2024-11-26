from django.utils import timezone
from videoconferencing_app.models import Meeting

def update_meeting_status():
    now = timezone.now()
    completed_meetings = Meeting.objects.filter(end_time__lt=now)
    # Optionally, perform any additional actions on completed meetings
