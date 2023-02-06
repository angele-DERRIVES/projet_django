from django.db import models
from django.contrib.auth.models import User

from Genealogie.models.quiz import Quiz


class Module(models.Model):
    title = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='module_owner')
    hours = models.PositiveIntegerField()
    quizzes = models.ManyToManyField(Quiz)

    def __str__(self):
        return self.title
