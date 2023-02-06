from django.shortcuts import render, redirect, get_object_or_404

from Genealogie.models.answer import Answer
from Genealogie.models.attempt import Attempt
from Genealogie.models.player import Player
from Genealogie.models.question import Question
from Genealogie.models.quiz import Quiz


def SubmitAttempt(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    user = request.user
    earned_points = 0

    if request.method == 'POST':
        questions = request.POST.getList('questions')
        answers = request.POST.getList('answers')
        player = Player.objects.create(user=user, quiz=quiz, score=0)

        for q, a in zip(questions, answers):
            question = Question.objects.get(id=q)
            answer = Answer.objects.get(id=a)
            Attempt.objects.create(quiz=quiz, player=player, question=question, answer=answer)

            if answer.is_correct == True:
                earned_points += question.points
                player.score += earned_points
                player.save()

        return redirect('index')
