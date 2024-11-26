from django.db import models
from django.utils import timezone

class Meeting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    link = models.URLField(blank=True, null=True)

    def is_completed(self):
        return self.end_time < timezone.now()

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
