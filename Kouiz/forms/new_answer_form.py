from django import forms

from Kouiz.models.answer import Answer


class NewAnswerForm(forms.ModelForm):
    answer_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
    # is_correct = forms.BooleanField()
    quiz_id = forms.IntegerField(widget=forms.HiddenInput())
    question_id = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Answer
        fields = ('answer_text', 'is_correct', 'quiz_id', 'question_id')
