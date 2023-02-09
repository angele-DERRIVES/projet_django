from django import forms

from Kouiz.models.question import Question


class NewQuestionForm(forms.ModelForm):
    question_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
    points = forms.IntegerField(max_value=100, min_value=1)

    class Meta:
        model = Question
        fields = ('question_text', 'points', 'answer1_text', 'answer1_is_correct', 'answer2_text', 'answer2_is_correct'
                  , 'answer3_text', 'answer3_is_correct', 'answer4_text', 'answer4_is_correct')
