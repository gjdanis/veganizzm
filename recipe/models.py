from django.db import models

class Ingredient(models.Model):
    """
    An ingredient is a food, drink, spice, etc. used in a recipe.

    Attributes:
        name (str): name of the ingredient (e.g. 'water')
    """
    name = models.CharField(max_length=100)

#TODO: put these somewhere else? Will want to tag posts as well.
class Tag(models.Model):
    """
    A tag is a label used to categorize and for sorting.

    Attributes:
        name (str): name of the tag (e.g. 'dessert')
        category (str): 'cooking methods', 'courses', 'dietary',
            'key ingredients', 'seasons', 'cuisine', 'dessert types', or
            'occasion'
    """

    class Categories:
        (cooking_methods, courses, dietary, key_ingredients, seasons, cuisine,
         dessert_types, occasion) = range(8)

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=1,
        choices=(
            (Categories.cooking_methods, 'cooking methods'),
            (Categories.courses, 'courses'),
            (Categories.dietary, 'dietary'),
            (Categories.key_ingredients, 'key ingredients'),
            (Categories.seasons, 'seasons'),
            (Categories.cuisine, 'cuisine'),
            (Categories.dessert_types, 'dessert types'),
            (Categories.occasion, 'occasion'),
        ),
        null=True,
        blank=True
    )

class Recipe(models.Model):
    """
    A recipe is a list of recipe steps along with some metadata. It does not
    actually contain any RecipeSteps; instead, each RecipeStep has a ForeignKey
    to a Recipe.

    Attributes:
        prep_time (duration): time needed for preparation
        cooking_time (duration): time needed for cooking
        total_time (duration): total time needed to make the recipe
        title (str): title of the recipe
        description (str): description of the recipe
        serves (int): number of servings made by the recipe
        source (str): where the recipe came from
        tags ([Tag]): tags for the recipe
        miscellaneous_info (str): any information not contained in the above

    Relationships:
        The relationship with the RecipeSteps is handled in RecipeStep
    """
    prep_time    = models.DurationField()
    cooking_time = models.DurationField()
    total_time   = models.DurationField()

    title  = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    serves = models.PositiveSmallIntegerField()
    source = models.CharField(max_length=1000)

    tags = models.ManyToManyField(Tag)
    miscellaneous_info = models.CharField(max_length=1000)

class RecipeStep(models.Model):
    """
    A recipe step is a numbered step in a recipe.

    Attributes:
        recipe: ([Recipe]): associated recipe
        index (int): ordering in the recipe
        instruction (str): what to do in the step

    Relationships:
        The relationship with the IngredientQuantities is handled in IngredientQuantity.
    """

    class Meta:
        default_related_name = 'recipe_step_set'

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(default=0)
    instruction = models.CharField(max_length=1000)

# TODO: min_value=0.0 not allowed by django??
# TODO: add field for countability for miscellaneous physical quantities?
# Consider 'two dashes salt' versus 'two handfuls strawberries.'
class IngredientQuantity(models.Model):
    """
    An ingredient quantity is an amount of a particular ingredient.

    Attributes:
        ingredient ([Ingredient]): associated ingredient
        recipe_step ([RecipeStep]): associated recipe step
        index (int): ordering in the recipe step
        physical_quantity (str): 'length', 'area', 'volume', 'mass', 'count',
            'miscellaneous'
        measure (float): amount (in base units for `physical_quantity`) of
            `ingredient`

            The base units are as follows:
                length          meter
                area            square meter
                volume          cubic meter
                mass            kilogram
                count           N/A
                miscellaneous   N/A

        unit_name (str|null): if `physical_quantity` is 'miscellaneous',
            name of unit used to measure `ingredient` (e.g. 'stalk')
        preparation (str|null): how the ingredient is to be prepared
    """

    class Meta:
        default_related_name = 'ingredient_quantity_set'
        verbose_name_plural = 'ingredient quantities'

    class PhysicalQuantities:
        length, area, volume, mass, count, miscellaneous = range(6)

    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    recipe_step = models.ForeignKey(RecipeStep, on_delete=models.CASCADE)
    index = models.PositiveSmallIntegerField(default=0)
    physical_quantity = models.CharField(
        max_length=1,
        choices=(
            (PhysicalQuantities.length, 'length'),
            (PhysicalQuantities.area, 'area'),
            (PhysicalQuantities.volume, 'volume'),
            (PhysicalQuantities.mass, 'mass'),
            (PhysicalQuantities.count, 'count'),
            (PhysicalQuantities.miscellaneous, 'miscellaneous'),
        )
    )
    measure = models.FloatField()
    unit_name = models.CharField(null=True, blank=True, max_length=100)
    preparation = models.CharField(null=True, blank=True, max_length=100)
