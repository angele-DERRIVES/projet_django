from django.urls import reverse
from django.views.generic import CreateView

from Kouiz.forms.new_quiz_form import NewQuizForm
from Kouiz.models.quiz import Quiz


class NewQuiz(CreateView):
    model = Quiz
    template_name = "Quiz/newQuiz.html"
    form_class = NewQuizForm

    def get_success_url(self):
        question_name = 'new_question'
        return reverse('new_question', args=[self.object.id])

        #return redirect('new_question', quiz_id=quiz.id)
