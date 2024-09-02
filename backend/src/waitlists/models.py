from django.db import models

class WaitlistEntry(models.Model):
    emails = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)