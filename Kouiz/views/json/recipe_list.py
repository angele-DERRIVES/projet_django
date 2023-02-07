from django.http import JsonResponse
from django.views import View

from Kouiz.models.recipes_content.recipe import Recipe


class RecipeListJsonView(View):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        result = Recipe.objects.all()
        return JsonResponse([a.title for a in result], safe=False)
