from django.contrib import admin

from Genealogie.models.ingredient import Ingredient
from Genealogie.models.recipe import Recipe
from Genealogie.models.recipe_ingredient_unit import RecipeIngredientUnit
from Genealogie.models.tag import Tag
from Genealogie.models.unit import Unit

admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(RecipeIngredientUnit)
