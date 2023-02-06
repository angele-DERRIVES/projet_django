from Genealogie.models import Module
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from Genealogie.models_directory.new_quiz_form import NewQuizForm
from Genealogie.models_directory.quiz import Quiz


def NewQuiz(request, module_id):
    user = request.user
    module = get_object_or_404(Module, id=module_id)

    if request.method == 'POST':
        form = NewQuizForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('title')
            due = form.cleaned_data.get('due')
            allowed_attempts = form.cleaned_data.get('allowed_attempts')
            time_limit_mins = form.cleaned_data.get('time_limit_mins')
            quiz = Quiz.objects.create(title=title, description=description, due=due,
                                       allowed_attempts=allowed_attempts, time_limit_mins=time_limit_mins)
            module.quizzes.add(quiz)
            module.save()

            return redirect('new-question', quiz_id=quiz.id)

    else:
        form = NewQuizForm()

    context = {
        'form': form
    }
    return render(request, 'Quiz/newQuiz.html', context)
