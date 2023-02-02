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
from django.urls import path

from Genealogie.views.index_view import IndexView
from Genealogie.views.recipe_detail_view import RecipeDetailView
from Genealogie.views.recipe_list_view import RecipeListView
from Genealogie.views.recipe_search_view import RecipeSearchView
from Genealogie.views.recipe_search_by_ingredient_view import RecipeSearchByIngredientView
from Genealogie.views.register_form import RegisterFormView

from Genealogie.views.tag_list_view import TagListView
from Genealogie.views.tag_detail_view import TagDetailView
from Genealogie.views.tag_create_view import TagCreateView
from Genealogie.views.tag_update_view import TagUpdateView
from Genealogie.views.json.recipe_list import RecipeListJsonView
from Accounts.Views.Register import register


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

    path('register_form/', register, name="register")
]
