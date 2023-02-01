from django.views.generic import ListView

from Genealogie.models.recipe import Recipe


class RecipeSearchView(ListView):
    template_name = 'recipe_list_view.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        result = super().get_context_data(object_list=object_list, **kwargs)
        result['description_results'] = \
            "Search result of Recipes with title '{}'".format(self.kwargs['search'])
        return result

    def get_queryset(self):
        return Recipe.objects.filter(title__icontains=self.kwargs['search'])
