from django.shortcuts import render, redirect, get_object_or_404

from Kouiz.models.player import Player
from Kouiz.models.question import Question
from Kouiz.models.quiz import Quiz


def QuizDetail(request, quiz_id):
    user = request.user
    quiz = Quiz.objects.get(id=quiz_id)
    questions = quiz.questions.all()

    context = {
        'quiz': quiz,
        'quiz_id': quiz_id,
        'questions': questions
    }
    return render(request, 'Quiz/quizDetail.html', context)
