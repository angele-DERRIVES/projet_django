from django.shortcuts import render, get_object_or_404

from Kouiz.models.answer import Answer
from Kouiz.models.question import Question
from Kouiz.models.quiz import Quiz


def QuestionDetail(request, quiz_id, question_id):
    quiz = Quiz.objects.get(id=quiz_id)
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question)
    context = {
        'quiz': quiz,
        'quiz_id': quiz_id,
        'question': question,
        'question_id': question_id,
        'answers': answers
    }
    return render(request, 'Quiz/questionDetail.html', context)
