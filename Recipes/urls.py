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
from Kouiz.views.new_answer_view import NewAnswerView
from Kouiz.views.new_quiz_view import NewQuiz
from Kouiz.views.question_detail_view import QuestionDetail
from Kouiz.views.quiz_list_view import QuizListView
from Kouiz.views.recipes_content.recipe_detail_view import RecipeDetailView
from Kouiz.views.recipes_content.recipe_list_view import RecipeListView
from Kouiz.views.recipes_content.recipe_search_view import RecipeSearchView
from Kouiz.views.recipes_content.recipe_search_by_ingredient_view import RecipeSearchByIngredientView
from Registration.Views.login_view import UserLoginView
from Registration.Views.register_form_view import RegisterFormView

from Kouiz.views.recipes_content.tag_list_view import TagListView
from Kouiz.views.recipes_content.tag_detail_view import TagDetailView
from Kouiz.views.recipes_content.tag_create_view import TagCreateView
from Kouiz.views.recipes_content.tag_update_view import TagUpdateView
from Kouiz.views.json.recipe_list import RecipeListJsonView

from Kouiz.views.attempt_detail_view import AttemptDetail
from Kouiz.views.new_question_view import NewQuestion
from Kouiz.views.quiz_detail_view import QuizDetail
from Kouiz.views.submit_attempt_view import SubmitAttempt
from Kouiz.views.take_quiz_view import TakeQuiz
from Kouiz.views.my_quiz_view import MyQuizView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('Recipes/list', RecipeListView.as_view(), name='recipes_list'),
    path('Recipes/details/<int:pk>', RecipeDetailView.as_view(), name='recipes_search'),
    path('Recipes/search/<str:search>', RecipeSearchView.as_view(), name='recipes_search_by_ingredient'),
    path('Recipes/search/by_ingredient/<str:search>',
         RecipeSearchByIngredientView.as_view(), name='recipes_detail'),

    path('tags/list', TagListView.as_view(), name='tag_list'),
    path('tags/details/<int:pk>', TagDetailView.as_view(), name='tag_detail'),
    path('tags/create', TagCreateView.as_view(), name='tag_create_view'),
    path('tags/update/<int:pk>', TagUpdateView.as_view(), name='tag_update'),

    path('json/Recipes/List/', RecipeListJsonView.as_view(), name='recipe_list_json'),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

    path('quiz/<int:quiz_id>/<int:attempt_id>/results', AttemptDetail, name='attempt_detail'),
    path('quiz/<int:quiz_id>/new_question/', NewQuestion, name='new_question'),
    # path('quiz/<int:quiz_id>/new_question/<int:key_id>/', NewQuestion, name='new_question_again'),
    path('quiz/new_quiz/', NewQuiz.as_view(), name='new_quiz'),
    path('quiz/<int:quiz_id>/', QuizDetail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/take/submit', SubmitAttempt, name='submit_attempt'),
    path('quiz/<int:quiz_id>/take', TakeQuiz, name='take_quiz'),
    path('quiz/list/', QuizListView.as_view(), name='quiz_list'),
    path('quiz/my_quizzes/', MyQuizView.as_view(), name='my_quizzes'),
    path('quiz/<int:quiz_id>/question/<int:question_id>/new_answer', NewAnswerView.as_view(), name='new_answer'),
    path('quiz/<int:quiz_id>/question/<int:question_id>', QuestionDetail, name='question_detail'),
]
