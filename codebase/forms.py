from .models import Event
from django import forms

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_description', 'location', 'event_category', 'timezone', 'event_date', 'event_time', 'image', 'website_url', 'instagram_handle']
