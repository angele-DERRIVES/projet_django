from django.db import models
from django.contrib.auth.models import User

from Genealogie.models.quiz import Quiz


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = user = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()
    completed = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
