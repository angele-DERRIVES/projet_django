from django.db import models
from django.contrib.auth.models import User

class Answer(models.Model):
    answer_text = models.CharField(max_lenght=900)
    is_correct = models.BooleanField()