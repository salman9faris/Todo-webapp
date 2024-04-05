from django.db import models

# Create your models here.
class Task(models.Model):
    task=models.CharField(max_length=255)
    is_complted=models.BooleanField(default=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return str(self.task)