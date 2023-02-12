"""Recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from Kouiz.views.index_view import IndexView
from Kouiz.views.new_answer_view import NewAnswer
from Kouiz.views.new_quiz_view import NewQuiz
from Kouiz.views.question_detail_view import QuestionDetail
from Kouiz.views.quiz_list_view import QuizListView
from Registration.Views.login_view import UserLoginView
from Registration.Views.register_form_view import RegisterFormView

from Kouiz.views.attempt_detail_view import AttemptDetail
from Kouiz.views.new_question_view import NewQuestion
from Kouiz.views.quiz_detail_view import QuizDetail
from Kouiz.views.submit_attempt_view import SubmitAttempt
from Kouiz.views.take_quiz_view import TakeQuiz
from Kouiz.views.my_quiz_view import MyQuizView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

    path('quiz/list/', QuizListView.as_view(), name='quiz_list'),

    path('quiz/<int:quiz_id>/take', TakeQuiz, name='take_quiz'),
    path('quiz/<int:quiz_id>/take/results', SubmitAttempt, name='submit_attempt'),
    path('quiz/<int:quiz_id>/<int:attempt_id>/results', AttemptDetail, name='attempt_detail'),

    path('quiz/my_quizzes/', MyQuizView.as_view(), name='my_quizzes'),
    path('quiz/new_quiz/', NewQuiz.as_view(), name='new_quiz'),
    path('quiz/<int:quiz_id>/new_question/', NewQuestion, name='new_question'),
    path('quiz/<int:quiz_id>/', QuizDetail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/question/<int:question_id>', QuestionDetail, name='question_detail'),
    path('quiz/<int:quiz_id>/question/<int:question_id>/new_answer', NewAnswer, name='new_answer'),
]
