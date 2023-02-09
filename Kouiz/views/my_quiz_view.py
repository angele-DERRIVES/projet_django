from django.views.generic import ListView

from Kouiz.models.quiz import Quiz


class MyQuizView(ListView):
    template_name = 'Quiz/MyQuizView.html'
    model = Quiz

    def get_queryset(self):
        return Quiz.objects.filter(user=self.request.user)
