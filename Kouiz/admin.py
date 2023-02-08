from django.contrib import admin

from Kouiz.models.answer import Answer
from Kouiz.models.attempt import Attempt
from Kouiz.models.player import Player
from Kouiz.models.question import Question
from Kouiz.models.quiz import Quiz
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

admin.site.register(Quiz)
admin.site.register(Answer)
admin.site.register(Attempt)
admin.site.register(Player)
admin.site.register(Question)

