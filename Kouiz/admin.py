from django.contrib import admin

from Kouiz.models.recipes_content.ingredient import Ingredient
from Kouiz.models.recipes_content.recipe import Recipe
from Kouiz.models.recipes_content.recipe_ingredient_unit import RecipeIngredientUnit
from Kouiz.models.recipes_content.tag import Tag
from Kouiz.models.recipes_content.unit import Unit

admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(RecipeIngredientUnit)
