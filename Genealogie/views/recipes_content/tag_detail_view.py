from django.views.generic import DetailView

from Genealogie.models.recipes_content.tag import Tag


class TagDetailView(DetailView):
    template_name = 'Recipes/tag_detail_view.html'
    model = Tag
