from django.db                import models
from datetime                 import timedelta
from django.core.urlresolvers import reverse
from veganizzm.utilities      import generate_slug

# == `Recipe` ==
class Recipe(models.Model):
    # A `Recipe` is a list of recipe steps. It doesn't actually 
    # contain any `RecipeStep` objects. Instead, each `RecipeStep`
    # has a foreign key to a `Recipe`.

    title  = models.CharField(max_length=255)
    slug   = models.SlugField(max_length=100, unique=True)
    serves = models.PositiveSmallIntegerField(default=1)
    source = models.CharField(null=True, blank=True, max_length=1000)
    description  = models.TextField()
    prep_time    = models.DurationField(default=timedelta())
    cooking_time = models.DurationField(default=timedelta())
    total_time   = models.DurationField(default=timedelta())

    # Override the `save` function to auto generate the `slug` field.
    def save(self, *args, **kwargs):
        self.slug = generate_slug(Recipe, self.title)
        return super(Recipe, self).save(*args, **kwargs)

    # Override the `get_absolute_url` to provide a preview link on the admin page.
    def get_absolute_url(self):
        return reverse('recipe_view', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

# == `Ingredient` ==
class Ingredient(models.Model):
    # An `Ingredient` models a recipe ingredient.

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# == `RecipeStep` ==
class RecipeStep(models.Model):
    # A `RecipeStep` is a numbered step in a `Recipe`. 
    # The object's `description` text should reference the parent `Recipe` object's
    # `IngredientQuantity` objects, though there's no foreign key relationship dictating
    # how this should be done.

    class Meta:
        default_related_name = 'recipe_step_set'

    recipe = models.ForeignKey(Recipe)
    number = models.PositiveSmallIntegerField()
    description = models.TextField()

# == `IngredientQuantity` ==
class IngredientQuantity(models.Model):
    # An `IngredientQuantity` is a measure of a particular 
    # `Ingredient` in a `Recipe`.

    class Meta:
        default_related_name = 'ingredient_quantity_set'
        verbose_name_plural  = 'ingredient quantities'

    class PhysicalUnit:
        length, volume, mass, count, miscellaneous = range(5)

    # `measure` is the amount (in base units of `physical_unit`) of `ingredient`.
    # If `physical_unit` is "miscellaneous", then `unit_name`
    # is used to measure `ingredient` (e.g. "stalk").
    measure   = models.FloatField()
    unit_name = models.CharField(null=True, blank=True, max_length=100)
    physical_unit = models.CharField(
        null=True,
        max_length=1,
        choices=(
            (PhysicalUnit.length, 'length'), # meters
            (PhysicalUnit.volume, 'volume'), # cubic meter
            (PhysicalUnit.mass, 'mass'),     # kilograms
            (PhysicalUnit.count, 'count'), 
            (PhysicalUnit.miscellaneous, 'miscellaneous')
        )
    )

    # `ingredient` is the `Ingredient` measured; `preparation` should indicate how it's prepared (e.g. chopped).
    ingredient  = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    preparation = models.CharField(null=True, blank=True, max_length=100)
    
    # `recipe` is the `Recipe` to which this `IngredientQuantity` belongs.
    # Expect deleting a `Recipe` to delete all associated `IngredientQuantity`
    # objects but leave the `Ingredient` objects untouched.
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

