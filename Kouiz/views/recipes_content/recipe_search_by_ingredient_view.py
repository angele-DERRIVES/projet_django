from django.db.models import Q
from django.views.generic import ListView

from Kouiz.models.recipes_content.recipe import Recipe


class RecipeSearchByIngredientView(ListView):
    template_name = 'Recipes/recipe_list_view.html'

    def get_queryset(self):
        search = self.kwargs['search']
        return Recipe.objects.filter(
            Q(ingredients_unit__ingredient__name_singular__icontains=search) |
            Q(ingredients_unit__ingredient__name_plural__icontains=search)
        )
