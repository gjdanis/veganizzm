from django.db import models

class Ingredient(models.Model):
    """
    An ingredient is a string that may be used with a quantity in a recipe

    Attributes:
        name (str): anything, e.g. 'water'
    """
    name = models.CharField(max_length=100)

# todo: min_value=0.0 not allowed by django??
# todo: populate picklist for units, preparation
class IngredientQuantity(models.Model):
    """
    An ingredient quantity is a prepared ingredient with a measured quantity

    Attributes:
        ingredient (Ingredient): to include
        quantity (float): the measured amount of the ingredient
        units (str): 'tablespoon', 'tsp', 'cup', 'qt'
    """
    
    class Units:
        tablespoon, teaspoon, cup, quart = range(1, 5)

    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField() 
    units = models.CharField(      
        max_length=1,
        choices=(
            (Units.tablespoon, "tablespoon"),
            (Units.teaspoon, "teaspoon"),
            (Units.cup, "cup"),
            (Units.quart, "quart"),
        )
    )

    class Meta:
        verbose_name_plural = "ingredient quantities"
    
class RecipeStep(models.Model):
    """
    A recipe step is a numbered step in a recipe

    Attributes:
        step_number (int): ordering of the step in the recipe
        ingredient_quantities ([IngredientQuantity]): the ingredient quantities to include
        description (str|null): text content of what to do for this step
    """

    step_number = models.PositiveSmallIntegerField(default=1)
    ingredient_quantities = models.ManyToManyField(IngredientQuantity)
    description = models.TextField(null=True)

# todo: populate picklist for courses
class Recipe(models.Model):
    """
    A recipe is a collection of recipe steps

    Attributes:
        receipe_steps ([RecipeStep]): what to do for this recipe
        name (str): e.g. 'Vegan Grapefruit Cupcakes with Bourbon Vanilla Frosting'
        description (str|null): blurb of what this recipe is
    """

    class CookingMethods:
        bake, blender, juice, raw, slow, fry, roast, grill, saute = range(1, 10)

    class DietaryRestrictions:
        vegan, vegetarian, low_carb, no_nuts, no_soy, no_gluten = range(1, 7)

    receipe_steps = models.ManyToManyField(RecipeStep)
    name = models.CharField(max_length=100, blank=False, default="name needed")
    description = models.TextField(null=True)

    # recipe meta data for search/recommendations
    cooking_method = models.CharField(
        null = True,
        max_length=1,
        choices=(
            (CookingMethods.bake, "bake"),
            (CookingMethods.blender, "blender"),
            (CookingMethods.juice, "juice"),
            (CookingMethods.raw, "raw"),
            (CookingMethods.slow, "slow-cooker"),
            (CookingMethods.fry, "fry"),
            (CookingMethods.roast, "roast"),
            (CookingMethods.grill, "grill"),
            (CookingMethods.saute, "saute"),
        )
    )
    diet = models.CharField(
        null = True,
        max_length=1,
        choices=(
            (DietaryRestrictions.vegan, "vegan"),
            (DietaryRestrictions.vegetarian, "vegetarian"),
            (DietaryRestrictions.low_carb, "low-carb"),
            (DietaryRestrictions.no_nuts, "nut-free"),
            (DietaryRestrictions.no_soy, "soy-free"),
            (DietaryRestrictions.no_gluten, "gluten-free"),
        )
    )

