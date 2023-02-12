from django.shortcuts import get_object_or_404

from Kouiz.forms.new_answer_form import NewAnswerForm
from Kouiz.models.answer import Answer
from Kouiz.models.question import Question
from Kouiz.models.quiz import Quiz

# @login_required
from django.shortcuts import render, redirect


def NewAnswer(request, quiz_id, question_id):
    user = request.user
    quiz = get_object_or_404(Quiz, id=quiz_id)
    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        form = NewAnswerForm(request.POST)

        if form.is_valid():
            answer_text = form.cleaned_data.get('answer_text')
            is_correct = form.cleaned_data.get('is_correct')
            answer = Answer.objects.create(answer_text=answer_text, is_correct=is_correct, question=question)
            return redirect('question_detail', quiz_id=quiz.id, question_id=question_id)

    else:
        form = NewAnswerForm()

    context = {
        'form': form,
        'quiz': quiz,
        'question': question
    }
    return render(request, 'Quiz/newAnswer.html', context)
