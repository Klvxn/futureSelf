import uuid
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Letter(models.Model):

    class AudienceChoices(models.TextChoices):
        PUBLIC = 'public, but as anon'
        PRIVATE = 'private'

    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateField()
    date_posted = models.DateTimeField(auto_now_add=True)
    email_address = models.EmailField()
    audience = models.CharField(max_length=20, choices=AudienceChoices.choices)
    delivered = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date_posted',)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('letter:letter_detail', kwargs={'pk': self.id})
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)

    def get_time_travelled(self):
        now = datetime.today().date()
        return self.date_posted.date() - now