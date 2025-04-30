from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    @property
    def participant_count(self):
        return self.participation_set.filter(is_attending=True).count()
    
    class Meta:
        ordering = ['date']

class Participation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    is_attending = models.BooleanField(default=False)
    registered_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'event')
        
    def __str__(self):
        status = "participe" if self.is_attending else "ne participe pas"
        return f"{self.user.username} {status} à {self.event.title}"