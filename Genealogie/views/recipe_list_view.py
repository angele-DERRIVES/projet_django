from django.views.generic import ListView

from Genealogie.models.recipe import Recipe


class RecipeListView(ListView):
    template_name = 'recipe_list_view.html'
    model = Recipe
