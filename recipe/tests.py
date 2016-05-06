from recipe.models import Ingredient, IngredientQuantity, RecipeStep, Recipe
from django.test   import TestCase
from django.db.models.deletion import ProtectedError

class IngredientTests(TestCase):
    pass
    # fixtures = ['simple-data-model.json']

    # def test_delete_ingredient(self):
    #     water = Ingredient.objects.all()[0]
    #     error = "Can't delete an Ingredient that has an associated IngredientQuantity."
    #     with self.assertRaises(ProtectedError, msg=error):
    #         water.delete()

    #     volume_of_water = IngredientQuantity.objects.all()[0]
    #     volume_of_water.delete()
    #     water.delete()
    #     self.assertTrue(
    #         len(Ingredient.objects.all()) == 0,
    #         "Expect 'water' to be deleted"
    #     )

class IngredientQuantityTests(TestCase):
    pass
    # fixtures = ['simple-data-model.json']

    # def test_delete_ingredient_quantity(self):
    #     volume_of_water = IngredientQuantity.objects.all()[0]
    #     volume_of_water.delete()
    #     self.assertTrue(
    #         len(IngredientQuantity.objects.all()) == 0,
    #         "Expect 'volume_of_water' to be deleted"
    #     )
    #     self.assertTrue(
    #         len(Ingredient.objects.all()) > 0,
    #         "Expect deleting 'volume_of_water' to not delete 'water'"
    #     )
    #     self.assertTrue(
    #         len(RecipeStep.objects.all()) > 0,
    #         "Expect deleting 'volume_of_water' to not delete 'pour_water'"
    #     )

class RecipeStepTests(TestCase):
    pass
    # fixtures = ['simple-data-model.json']

    # def test_delete_recipe_step(self):
    #     pour_water = RecipeStep.objects.all()[0]
    #     pour_water.delete()
    #     self.assertTrue(
    #         len(RecipeStep.objects.all()) == 0,
    #         "Expect 'pour_water' to be deleted"
    #     )
    #     self.assertTrue(
    #         len(Ingredient.objects.all()) > 0,
    #         "Expect deleting 'pour_water' to not delete 'water'"
    #     )
    #     self.assertTrue(
    #         len(Recipe.objects.all()) > 0,
    #         "Expect deleting 'pour_water' to not delete 'glass_of_water'"
    #     )

class RecipeTests(TestCase):
    pass
    # fixtures = ['simple-data-model.json']

    # def test_delete_recipe(self):
    #     glass_of_water = Recipe.objects.all()[0]
    #     glass_of_water.delete()
    #     self.assertTrue(
    #         len(Recipe.objects.all()) == 0,
    #         "Expect 'glass_of_water' to be deleted"
    #     )
    #     self.assertTrue(
    #         len(glass_of_water.recipe_step_set.all()) == 0,
    #         "Expect deleting 'glass_of_water' to delete 'pour_water' used in "
    #             "'glass_of_water'"
    #     )
