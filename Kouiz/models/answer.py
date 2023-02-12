from django.db import models
from django.contrib.auth.models import User

from Kouiz.models.question import Question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.CharField(max_length=900)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text
