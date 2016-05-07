from recipe.models import Ingredient, IngredientQuantity, RecipeStep, Recipe, RecipeEquipment
from django.test   import TestCase
from django.db.models.deletion import ProtectedError

class TestIngredient(TestCase):
    fixtures = ['recipe-test-models.json']

    def test_delete_ingredient(self):
        ingredient = Ingredient.objects.get(name="water")
        error = "Can't delete an Ingredient that has an associated IngredientQuantity."
        
        with self.assertRaises(ProtectedError, msg=error):
            ingredient.delete()
        
        ingredient_quantities = IngredientQuantity.objects.filter(ingredient__name="water")
        for ingredient_quantity in ingredient_quantities:
            ingredient_quantity.delete()

        ingredient = Ingredient.objects.get(name="water")
        ingredient.delete()
        
        ingredient_quantities = IngredientQuantity.objects.filter(ingredient__name="water")
        self.assertTrue(len(ingredient_quantities) == 0, "Expect 'ingredient_quantities' to be deleted")

class TestIngredientQuantity(TestCase):
    fixtures = ['recipe-test-models.json']

    def test_delete_ingredient_quantity(self):
        ingredient_quantities = IngredientQuantity.objects.filter(ingredient__name="water")
        for ingredient_quantity in ingredient_quantities:
            ingredient_quantity.delete()

        ingredient_quantities = IngredientQuantity.objects.filter(ingredient__name="water")
        self.assertTrue(len(ingredient_quantities) == 0, "Expect 'ingredient_quantities' to be deleted")

        ingredient = Ingredient.objects.get(name="water")
        self.assertIsNotNone(ingredient, "Expect deleting 'ingredient_quantities' to not delete 'ingredient'")

class TestRecipeStep(TestCase):
    fixtures = ['recipe-test-models.json']

    def test_delete_recipe_step(self):
        recipe_steps = RecipeStep.objects.filter(recipe__title="Glazed Cinnamon Buns")
        for recipe_step in recipe_steps:
            recipe_step.delete()

        recipe = Recipe.objects.get(title="Glazed Cinnamon Buns")
        self.assertIsNotNone(recipe, "Expect deleting 'recipe_steps' to not delete 'recipe'")

        ingredient_quantities = IngredientQuantity.objects.filter(recipe__title="Glazed Cinnamon Buns")
        self.assertTrue(
            len(ingredient_quantities) > 0,
            "Expect deleting 'recipe_steps' to not delete 'ingredient_quantities"
        )

class RecipeTests(TestCase):
    fixtures = ['recipe-test-models.json']

    def test_delete_recipe(self):
        recipe_equipment = RecipeEquipment.objects.get(name='aluminum foil')
        recipe = Recipe.objects.get(title="Peanut Butter Cinnamon Baked Apples")
        recipe.delete()

        self.assertIsNotNone(
            RecipeEquipment.objects.get(name='aluminum foil'),
            "Expect deleting 'recipe' to leave 'recipe_equipment' unchanged"
        )

        ingredient_quantities = IngredientQuantity.objects.filter(recipe__title="Peanut Butter Cinnamon Baked Apples")
        self.assertTrue(
            len(ingredient_quantities) == 0,
            "Expect deleting 'recipe' to delete 'ingredient_quantities'"
        )

        recipe_steps = RecipeStep.objects.filter(recipe__title="Peanut Butter Cinnamon Baked Apples")
        self.assertTrue(
            len(ingredient_quantities) == 0,
            "Expect deleting 'recipe' to delete 'recipe_steps'"
        )


