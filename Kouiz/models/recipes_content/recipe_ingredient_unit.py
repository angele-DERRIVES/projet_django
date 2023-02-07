from django.db import models

from Kouiz.models.recipes_content.ingredient import Ingredient
from Kouiz.models.recipes_content.recipe import Recipe
from Kouiz.models.recipes_content.unit import Unit


class RecipeIngredientUnit(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               related_name='ingredients_unit')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    value = models.FloatField(default=1.0)
    unit_is_displayed = models.BooleanField(default=True)

    def __str__(self):
        if not self.unit_is_displayed:
            return f"{self.recipe} / {self.value} {self.ingredient}"
        return f"{self.recipe} / {self.value} - {self.unit} {self.ingredient}"