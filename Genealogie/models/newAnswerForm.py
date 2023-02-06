from django import forms

from Genealogie.models.answer import Answer


class NewAnswerForm(forms.ModelForm):
    answer_text = forms.CharField(widget=forms.TextInput(attrs={'class': 'validate'}), required=True)
    is_correct = forms.BooleanField(required=True)

    class Meta:
        model = Answer
        fields = ('answer_text', 'is_correct')
