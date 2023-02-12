from django.contrib import admin

from Kouiz.models.answer import Answer
from Kouiz.models.attempt import Attempt
from Kouiz.models.player import Player
from Kouiz.models.question import Question
from Kouiz.models.quiz import Quiz

admin.site.register(Quiz)
admin.site.register(Answer)
admin.site.register(Attempt)
admin.site.register(Player)
admin.site.register(Question)

