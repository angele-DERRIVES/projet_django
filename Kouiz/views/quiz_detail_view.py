from django.shortcuts import render

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
