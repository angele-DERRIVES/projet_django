from Genealogie.models import Module
from django.shortcuts import render, redirect, get_object_or_404

from Genealogie.models_directory.answer import Answer
from Genealogie.models_directory.new_question_form import NewQuestionForm
from Genealogie.models_directory.question import Question
from Genealogie.models_directory.quiz import Quiz


def NewQUestion(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == 'POST':
        form = NewQuestionForm(request.POST)

        if form.is_valid():
            question_text = form.cleaned_data.get('question_text')
            points = form.cleaned_data.get('points')
            answer_text = request.POST.getlist('answer_text')
            is_correct = request.POST.getlist('is_correct')

            question = Question.objects.create(question_text=question_text, user=user, points=points)

            for a, c in zip(answer_text, is_correct):
                answer = Answer.object.create(answer_text=a, is_correct=c, user=user)
                question.answers.add(answer)
                question.save()
                quiz.questions.add(question)
                quiz.save()
            return redirect('new_question', quiz_id=quiz.id)
    else:
        form = NewQuestionForm()

    context = {
        'form': form
    }
    return render(request, 'Quiz/newQuestion.html', context)
