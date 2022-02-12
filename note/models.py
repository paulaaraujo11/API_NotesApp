from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    deadline_date = models.DateField()
    enabled = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title