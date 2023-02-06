from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    answer_text = models.CharField(max_lenght=900)
    is_correct = models.BooleanField(default=False)  # Only one answer is correct
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text
