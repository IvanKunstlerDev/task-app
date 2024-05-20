from django.db import models

class Task(models.Model):
    body = models.CharField(max_length=80, blank=False, null=False)
    is_completed = models.BooleanField(default=False)