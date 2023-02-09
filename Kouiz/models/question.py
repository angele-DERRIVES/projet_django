from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=900)
    points = models.PositiveIntegerField()

    answer1_text = models.CharField(max_length=900)
    answer1_is_correct = models.BooleanField(default=False)

    answer2_text = models.CharField(max_length=900)
    answer2_is_correct = models.BooleanField(default=False)

    answer3_text = models.CharField(max_length=900)
    answer3_is_correct = models.BooleanField(default=False)

    answer4_text = models.CharField(max_length=900)
    answer4_is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text
