from django.views.generic import DetailView

from Genealogie.models_directory.tag import Tag


class TagDetailView(DetailView):
    template_name = 'Recipes/tag_detail_view.html'
    model = Tag
