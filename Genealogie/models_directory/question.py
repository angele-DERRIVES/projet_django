from django.db import models
from django.contrib.auth.models import User

from Genealogie.models_directory.answer import Answer


class Question(models.Model):
    question_text = models.CharField(max_length=900)
    answers = models.ManyToManyField(Answer)  # Multiple answers to one question
    points = models.PositiveIntergerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text
