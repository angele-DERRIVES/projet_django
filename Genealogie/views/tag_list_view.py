from django.views.generic import ListView

from Genealogie.models.tag import Tag


class TagListView(ListView):
    template_name = 'Recipes/tag_list_view.html'
    model = Tag
