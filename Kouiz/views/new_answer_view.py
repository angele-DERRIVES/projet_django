from django.shortcuts import get_object_or_404

from django.views.generic import FormView

from Kouiz.forms.new_answer_form import NewAnswerForm

from Kouiz.models.answer import Answer
from Kouiz.models.question import Question
from Kouiz.models.quiz import Quiz

# @login_required
from django.shortcuts import render, redirect


class NewAnswerView(FormView):
    form_class = NewAnswerForm
    template_name = 'Quiz/newAnswer.html'

    def form_valid(self, form):
        answer_text = form.cleaned_data.get('answer_text')
        is_correct = form.cleaned_data.get('is_correct')
        quiz_id = self.kwargs['quiz_id']
        question_id = self.kwargs['question_id']
        user = self.request.user

        quiz = get_object_or_404(Quiz, id=quiz_id)
        question = get_object_or_404(Question, id=question_id)

        answer = Answer.objects.create(answer_text=answer_text, is_correct=is_correct, user=user)
        question.answers.add(answer)
        question.save()
        quiz.questions.add(question)
        quiz.save()

        return redirect('my_answers', quiz_id=quiz_id, question_id=question_id)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})
