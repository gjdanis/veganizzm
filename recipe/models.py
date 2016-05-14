from django.db                import models
from django.core.urlresolvers import reverse
from veganizzm.utilities      import generate_slug
from taggit.managers          import TaggableManager

# == `Recipe` ==
class Recipe(models.Model):
    # A `Recipe` is a list of recipe steps. It doesn't actually 
    # contain any `RecipeStep` objects. Instead, each `RecipeStep`
    # has a foreign key to a `Recipe`.

    title = models.CharField(max_length=255)
    slug  = models.SlugField(max_length=100, unique=True, editable=False)
    makes = models.PositiveSmallIntegerField(null=True, blank=True)

    # Optional preceding text for a `Recipe`.
    blurb = models.CharField(max_length=500, null=True, blank=True)

    # How long it takes to make this `Recipe`.
    prep_time    = models.DurationField(null=True, blank=True, help_text="An hh:mm:ss duration.")
    cooking_time = models.DurationField(null=True, blank=True, help_text="An hh:mm:ss duration.")

    # `RecipeEquipment` needed for this `Recipe`.
    recipe_equipment = models.ManyToManyField('RecipeEquipment')

    # Link to source of the recipe, if applicable.
    web_reference = models.URLField(null=True, blank=True, help_text="Web URL for citation purposes.")

    # Indexable tags.
    tags = TaggableManager(blank=True)

    # A recipe may be divided into sections. Each section should be modeled as 
    # another `Recipe` belonging to this `Recipe`.
    child_recipes = models.ManyToManyField(
        'self',
        help_text="Use if this recipe has multiple sub-recipes.",
        blank=True
    )

    # Override the `save` function to auto generate the `slug` field.
    def save(self, *args, **kwargs):
        self.slug = generate_slug(Recipe, self.title)
        return super(Recipe, self).save(*args, **kwargs)

    # Override the `get_absolute_url` to provide a preview link on the admin page.
    def get_absolute_url(self):
        return reverse('recipe_view', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

# == `Unit` ==
class Unit(models.Model):
    class Meta:
        ordering = ['long_name']

    PhysicalUnits = (
        (0, 'Other'),
        (1, 'Mass'),
        (2, 'Volume'),
    )

    Systems = (
        (0, 'N/A'),
        (1, 'SI'),
        (2, 'Imperial'),
    )

    # Name of the unit and short name of the unit (e.g. cups/c).
    # TODO: do we need a field for plurals?
    long_name  = models.CharField(max_length=60, unique=True)
    short_name = models.CharField(max_length=60, unique=True)
    
    # For conversion purposes. 
    physical_unit = models.IntegerField(choices=PhysicalUnits)
    system = models.IntegerField(choices=Systems) 

    def __str__(self):
        return self.short_name

# == `Ingredient` ==
class Ingredient(models.Model):
    # An `Ingredient` models a recipe ingredient.
    
    class Meta:
        ordering = ['name']
    
    name = models.CharField(max_length=255, unique=True)

    # External link to an example.
    web_reference = models.URLField(null=True, blank=True)

    def save(self):
        self.name = self.name.lower()
        super(Ingredient, self).save()

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

    number  = models.PositiveSmallIntegerField(null=True, blank=True)
    content = models.TextField()
    recipe  = models.ForeignKey(Recipe)

# == `RecipeEquipment` ==
class RecipeEquipment(models.Model):
    # Used to model equipment used in a `Recipe`.

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'recipe equipment'

    name = models.CharField(max_length=255, unique=True)
   
    # External link to an example.
    web_reference = models.URLField(null=True, blank=True, help_text="Web URL for citation purposes.")

    def save(self):
        self.name = self.name.lower()
        super(RecipeEquipment, self).save()

    def __str__(self):
        return self.name

# == `IngredientQuantity` ==
class IngredientQuantity(models.Model):
    # An `IngredientQuantity` is a measure of a particular 
    # `Ingredient` in a `Recipe`.

    class Meta:
        default_related_name = 'ingredient_quantity_set'
        verbose_name_plural  = 'recipe ingredient quantities'

    # `measure` is the amount (in base units of `physical_unit`) of `ingredient`.
    # It is a `CharField` to allow for fractions, and range quantities (e.g. 2-3)
    # 'unit' should reference a 'Unit', so we can convert, if needed.
    measure = models.CharField(max_length=10, null=True, blank=True)
    unit = models.ForeignKey(Unit, null=True, blank=True)

    # `ingredient` is the `Ingredient` measured; `preparation`
    # should indicate how it's prepared (e.g. chopped).
    ingredient  = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    preparation = models.CharField(null=True, blank=True, max_length=100)

    # `recipe` is the `Recipe` to which this `IngredientQuantity` belongs.
    # Expect deleting a `Recipe` to delete all associated `IngredientQuantity`
    # objects but leave the `Ingredient` objects untouched.
    recipe = models.ForeignKey(Recipe)

    def __str__(self):
        return "{0} {1} {2} {3}".format(
            self.measure,
            self.unit,
            self.ingredient,
            self.preparation
        )
