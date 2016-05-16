from recipe.models import Ingredient, IngredientQuantity, Recipe, RecipeEquipment, Unit
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

class RecipeTests(TestCase):
    fixtures = ['recipe-test-models.json']

    def test_delete_recipe(self):
        recipe_equipment = RecipeEquipment.objects.get(name="aluminum foil")
        recipe = Recipe.objects.get(title="Peanut Butter Cinnamon Baked Apples")
        recipe.delete()

        self.assertIsNotNone(
            RecipeEquipment.objects.get(name="aluminum foil"),
            "Expect deleting 'recipe' to leave 'recipe_equipment' unchanged"
        )

        ingredient_quantities = IngredientQuantity.objects.filter(recipe__title="Peanut Butter Cinnamon Baked Apples")
        self.assertTrue(
            len(ingredient_quantities) == 0,
            "Expect deleting 'recipe' to delete 'ingredient_quantities'"
        )

    def test_delete_recipe_with_children(self):
        recipe = Recipe.objects.get(title="Glazed Cinnamon Buns")
        recipe.delete()

        error = "Expect deleting 'recipe' to leave child recipes unchanged"
        self.assertIsNotNone(
            Recipe.objects.get(title="Cinnamon Buns"),
            error
        )

        self.assertIsNotNone(
            Recipe.objects.get(title="Cinnamon-Sugar Filling"),
            error
        )

        self.assertIsNotNone(
            Recipe.objects.get(title="Icing"),
            error
        )

class UnitTests(TestCase):
    fixtures = ['recipe-test-models.json']

    def test_delete_unit(self):
        unit = Unit.objects.get(short_name='C')
        ingredient_quantities = IngredientQuantity.objects.filter(unit__short_name='C')
        starting_count = len(ingredient_quantities)
        unit.delete()
        ingredient_quantities = IngredientQuantity.objects.filter(
            pk__in=[obj.pk for obj in ingredient_quantities]
        )

        self.assertTrue(
            len(ingredient_quantities) == starting_count and 
            all(obj.unit is None for obj in ingredient_quantities),
            "Expect deleteing 'unit' to leave 'ingredient_quantities' using 'unit' unchanged"
        )
        

