from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=900)
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.question_text
