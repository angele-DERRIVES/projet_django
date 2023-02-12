from django.shortcuts import render, redirect, get_object_or_404

from Kouiz.models.quiz import Quiz


def TakeQuiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)

    if request.method == 'POST':
        score = 0

        for question in quiz.questions.all():
            answers = request.POST.getlist('answers')
            for answer in question.answers.all():
                if answer.id in answers:
                    if answer.is_correct:
                        score += question.points
        # Enregistrer le score et afficher les résultats à l'utilisateur
        context = {
            'quiz': quiz,
            'score': score,
        }
        return render(request, 'Quiz/results.html', context)
    else:
        # Afficher le formulaire pour que l'utilisateur puisse répondre aux questions
        context = {
            'quiz': quiz,
        }
        return render(request, 'Quiz/takeQuiz.html', context)
