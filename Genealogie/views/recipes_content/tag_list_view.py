from django.views.generic import ListView

from Genealogie.models.recipes_content.tag import Tag


class TagListView(ListView):
    template_name = 'Recipes/tag_list_view.html'
    model = Tag
