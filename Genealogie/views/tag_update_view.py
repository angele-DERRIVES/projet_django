from django.urls import reverse
from django.views.generic import UpdateView

from Genealogie.models_directory.tag import Tag


class TagUpdateView(UpdateView):
    template_name = 'Recipes/tag_update_view.html'
    model = Tag
    fields = ['text']

    def get_success_url(self):
        return reverse('tag_list')
