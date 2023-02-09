from django.db import models
from django.contrib.auth.models import User

from Kouiz.models.question import Question


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    questions = models.ManyToManyField(Question)  # Multiple questions in one quiz

    def __str__(self):
        return self.title
