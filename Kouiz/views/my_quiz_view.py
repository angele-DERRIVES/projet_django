from django.views.generic import ListView

from Kouiz.models.quiz import Quiz


class MyQuizView(ListView):
    template_name = 'Quiz/MyQuizView.html'
    model = Quiz

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Quiz.objects.filter(user=self.request.user)
        return Quiz.objects.none()
