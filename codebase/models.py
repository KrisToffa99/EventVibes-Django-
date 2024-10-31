from django.db import models
from django.contrib.auth.models import User
import uuid

class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_when = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Password reset for {self.user.username} at {self.created_when}"
    
from django.db import models
from django.utils import timezone

class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_description = models.TextField()
    location = models.CharField(max_length=255)
    event_category = models.CharField(max_length=100)
    timezone = models.CharField(max_length=50)
    event_date = models.DateField()
    event_time = models.TimeField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    website_url = models.URLField(blank=True, null=True)
    instagram_handle = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.event_name
