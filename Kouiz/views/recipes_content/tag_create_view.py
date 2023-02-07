from django.urls import reverse
from django.views.generic import CreateView

from Kouiz.models.recipes_content.tag import Tag


class TagCreateView(CreateView):
    template_name = 'Recipes/tag_create_view.html'
    model = Tag
    fields = ['text']

    def get_success_url(self):
        return reverse('tag_list')