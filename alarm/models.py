from django.db import models

class Alarm(models.Model):
    time_go = models.TimeField()
    time_break = models.TimeField()
    time_longbreak = models.TimeField()
    enabled = models.BooleanField(default=True)

    def __str__(self) -> str:
        return super().__str__()
# Create your models here.
