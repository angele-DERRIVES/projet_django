from django.views.generic import DetailView

from Kouiz.models.recipes_content.recipe import Recipe


class RecipeDetailView(DetailView):
    template_name = 'Recipes/recipe_detail_view.html'
    model = Recipe
