from django.contrib import admin

from Genealogie.models_directory.ingredient import Ingredient
from Genealogie.models_directory.recipe import Recipe
from Genealogie.models_directory.recipe_ingredient_unit import RecipeIngredientUnit
from Genealogie.models_directory.tag import Tag
from Genealogie.models_directory.unit import Unit

admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Unit)
admin.site.register(RecipeIngredientUnit)
