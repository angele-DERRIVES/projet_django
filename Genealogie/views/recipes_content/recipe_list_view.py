from django.views.generic import ListView

from Genealogie.models.recipes_content.recipe import Recipe


class RecipeListView(ListView):
    template_name = 'Recipes/recipe_list_view.html'
    model = Recipe
