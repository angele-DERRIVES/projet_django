from django.urls import reverse
from django.views.generic import CreateView

from Kouiz.forms.new_quiz_form import NewQuizForm
from Kouiz.models.quiz import Quiz


class NewQuiz(CreateView):
    model = Quiz
    template_name = "Quiz/newQuiz.html"
    form_class = NewQuizForm

    def form_valid(self, form):
        title = form.cleaned_data.get('title')
        description = form.cleaned_data.get('description')

        form.instance.user = self.request.user

        quiz = Quiz.objects.create(title=title, description=description)
        # module.quizzes.add(quiz)
        # module.save()

        return super().form_valid(form)

    def get_success_url(self):
        reverse('home')

        #return redirect('new_question', quiz_id=quiz.id)


