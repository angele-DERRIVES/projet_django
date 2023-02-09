from django.views.generic import ListView

from Kouiz.models.quiz import Quiz


class QuizListView(ListView):
    template_name = 'Quiz/QuizListView.html'
    model = Quiz
