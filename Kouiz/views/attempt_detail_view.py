from django.shortcuts import render, redirect, get_object_or_404

from Kouiz.models.player import Player
from Kouiz.models.quiz import Quiz


def AttemptDetail(request, quiz_id, attempt_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    attempts = Player.objects.filter(quiz=quiz, player__user=user)

    context = {
        'quiz': quiz,
        'attempts': attempts
    }
    return render(request, 'Quiz/attemptDetail.html', context)
