from faulthandler import enable
from turtle import mode
from django.db import models
from note.models import Note

class Tasks(models.Model):
    description = models.CharField(max_length=50)
    note_id = models.ForeignKey(Note,on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)
    enabled = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.description