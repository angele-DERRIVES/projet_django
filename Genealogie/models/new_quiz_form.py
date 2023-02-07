from django import forms
from django.db import models
from ckeditor.widgets import CKEditorWidget

from Genealogie.models.quiz import Quiz


#class NewQuizForm(models.Model):
class NewQuizForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
    description = forms.CharField(widget=CKEditorWidget())
    due = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}), required=True)
    allowed_attempts = forms.IntegerField(max_value=100, min_value=1)
    time_limit_mins = forms.IntegerField(max_value=360, min_value=1)

    class Meta:
        model = Quiz
        fields = ('title', 'description', 'due', 'allowed_attempts', 'time_limit_mins')
