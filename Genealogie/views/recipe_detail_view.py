from django.views.generic import DetailView

from Genealogie.models.recipe import Recipe


class RecipeDetailView(DetailView):
    template_name = 'recipe_detail_view.html'
    model = Recipe
