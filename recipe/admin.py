from django.contrib import admin
from django.conf    import settings
from django.forms   import TextInput
from django         import forms
from recipe.models  import *
from django_summernote.widgets import SummernoteWidget

# Admin configuration for the `recipe` application. 
# Only `Unit`, `Ingredient`, `RecipeEquipment`, and `Recipe`
# are editable on admin. Everything else should be modified from within a `Recipe`.

class AdminInlineIngredientQuantityForm(forms.ModelForm):
    # Use `SummernoteWidget` for rich text editing.
    class Meta:
        model   = IngredientQuantity
        fields  = '__all__'
        widgets = {
            'measure': TextInput(attrs={'size': '5'}),
        }
    pass

class AdminInlineRecipeStepForm(forms.ModelForm):
    # Use `SummernoteWidget` for rich text editing.
    class Meta:
        model   = RecipeStep
        fields  = '__all__'
        widgets = {
            'content': SummernoteWidget(attrs={'width': '600px', 'height': '250px'}),
        }
    pass

class AdminRecipeForm(forms.ModelForm):
    # Use `SummernoteWidget` for rich text editing.
    class Meta:
        model   = Recipe
        fields  = '__all__'
        widgets = {
            'description': SummernoteWidget(attrs={'width': '600px', 'height': '250px'}),
        }
    pass

class AdminInlineRecipeSection(admin.TabularInline):
    extra = 0
    model = RecipeSection

class AdminInlineRecipeEquipment(admin.TabularInline):
    extra = 0
    model = Recipe.recipe_equipment.through
    model._meta.verbose_name_plural = "recipe equipment"
    model._meta.verbose_name = "equipment item"

class AdminInlineIngredientQuantity(admin.TabularInline):
    extra = 0
    model = IngredientQuantity
    form  = AdminInlineIngredientQuantityForm

class AdminInlineRecipeStep(admin.TabularInline):
    extra = 0
    model = RecipeStep
    form  = AdminInlineRecipeStepForm

@admin.register(Unit)
class AdminUnit(admin.ModelAdmin):
    list_display = [
        'long_name',
        'short_name',
        'physical_unit',
        'system',
    ]

@admin.register(Ingredient)
class AdminIngredient(admin.ModelAdmin):
    pass

@admin.register(RecipeEquipment)
class AdminRecipeEquipment(admin.ModelAdmin):
    pass

@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    inlines = [
        AdminInlineRecipeSection,
        AdminInlineRecipeEquipment,
        AdminInlineIngredientQuantity,
        AdminInlineRecipeStep,
    ]
    exclude = ['recipe_equipment',]
    form = AdminRecipeForm


