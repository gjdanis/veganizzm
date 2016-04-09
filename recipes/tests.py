from recipes.models import Ingredient, IngredientQuantity, RecipeStep, Recipe
from django.test import TestCase

class IngredientTests(TestCase):
	fixtures = ['sample-recipes.json']

	def test_delete_ingredient(self):
		water = Ingredient.objects.all()[0]
		water.delete()
		self.assertTrue(
			len(Ingredient.objects.all()) == 0,
			"Expect 'water' to be deleted"
		)
		self.assertTrue(
			len(IngredientQuantity.objects.all()) == 0,
			"Expect deleting 'water' to delete 'four_cups_water'"
		)
		self.assertTrue(
			len(RecipeStep.objects.all()[0].ingredient_quantities.all()) == 0,
			"Expect deleting 'water' to delete 'four_cups_water' used in 'add_water'"
		)

class IngredientQuantityTests(TestCase):
	fixtures = ['sample-recipes.json']

	def test_delete_ingredient_quantity(self):
		four_cups_water = IngredientQuantity.objects.all()[0]
		four_cups_water.delete()
		self.assertTrue(
			len(IngredientQuantity.objects.all()) == 0,
			"Expect 'four_cups_water' to be deleted"
		)
		self.assertTrue(
			len(Ingredient.objects.all()) > 0,
			"Expect deleting 'four_cups_water' to not delete 'water'"
		)
		self.assertTrue(
			len(RecipeStep.objects.all()) > 0,
			"Expect deleting 'four_cups_water' to not delete 'add_water'"
		)
		self.assertTrue(
			len(RecipeStep.objects.all()[0].ingredient_quantities.all()) == 0,
			"Expect deleting 'four_cups_water' to delete 'four_cups_water' used in 'add_water'"
		)

class RecipeTests(TestCase):
	fixtures = ['sample-recipes.json']
	
	def test_delete_recipe(self):
		self.assertTrue(1 == 1)
















