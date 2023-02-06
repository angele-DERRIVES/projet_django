from django.db import models
from django.contrib.auth.models import User

from Genealogie.models.answer import Answer
from Genealogie.models.player import Player
from Genealogie.models.question import Question
from Genealogie.models.quiz import Quiz


class Attempt(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.player.user.username + ' - ' + self.answer.answer_text
