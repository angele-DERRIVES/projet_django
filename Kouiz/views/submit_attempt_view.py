from django.shortcuts import render, redirect, get_object_or_404

from Kouiz.models.answer import Answer
from Kouiz.models.attempt import Attempt
from Kouiz.models.player import Player
from Kouiz.models.question import Question
from Kouiz.models.quiz import Quiz


def SubmitAttempt(request, quiz_id, question_id, answer_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question = get_object_or_404(Question, id=question_id)
    answer = get_object_or_404(Answer, id=answer_id)

    if request.method == 'POST':
        player, created = Player.objects.get_or_create(user=request.user, quiz=quiz)

        if answer.is_correct:
            player.score += question.points
            player.save()

        return redirect('results')

    return render(request, 'Quiz/takeQuiz.html', {'question': question})
