from django import forms
from django.db import models
from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm

from Kouiz.models.quiz import Quiz


#class NewQuizForm(models.Model):
class NewQuizForm(ModelForm):
    title = forms.CharField(required=True)
    description = forms.CharField()

    class Meta:
        model = Quiz
        fields = ('title', 'description')
        """widgets = {
            'due': forms.DateTimeInput(format='%Y-%m-%d',
                                       attrs={'type': 'datetime-local', 'class': 'timepicker'}),
        }"""
