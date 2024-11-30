from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class WaitlistEntry(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)