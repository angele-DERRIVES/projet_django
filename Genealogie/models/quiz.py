from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField

from Genealogie.models.question import Question


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    due = models.DateField()
    allowed_attempts = models.PositiveIntegerField()
    time_limit = models.PositiveIntegerField()
    questions = models.ManyToManyField(Question)  # Multiple questions in one quiz

    def __str__(self):
        return self.title

django.db.models_directory