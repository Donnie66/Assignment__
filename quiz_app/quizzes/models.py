from django.db import models

# Create your models here.
class Quiz(models.Model):
    question = models.CharField(max_length=255)
    options = models.JSONField()
    right_answer = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, default = 'inactive')
