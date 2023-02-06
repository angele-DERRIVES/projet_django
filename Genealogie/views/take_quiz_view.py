from django.shortcuts import render, redirect, get_object_or_404

from Genealogie.models_directory.quiz import Quiz


def TakeQuiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    context = {
        'quiz': quiz,
    }
    return render(request, 'Quiz/takeQuiz.html', context)
