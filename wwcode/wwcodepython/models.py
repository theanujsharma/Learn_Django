from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=64)
    speaker = models.CharField(max_length=64)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} will be presented by {self.speaker} on {self.date}"
