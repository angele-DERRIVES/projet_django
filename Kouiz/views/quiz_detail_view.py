from django.shortcuts import render, redirect, get_object_or_404

from Kouiz.models.player import Player
from Kouiz.models.quiz import Quiz


def QuizDetail(request, quiz_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)

    context = {
        'quiz': quiz
    }
    return render(request, 'Quiz/quizDetail.html', context)
