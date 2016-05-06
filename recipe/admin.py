from django.contrib import admin
from django.conf    import settings
from django.forms   import TextInput
from django         import forms
from recipe.models  import *

# Admin configuration for the `recipe` application. 
# Only `Recipe`, `RecipeTag`, `Ingredient`, and `Unit` are editable on admin. `RecipeStep`
# and `IngredientQuantity` should be created or modified inline
# from a `Recipe`.

class AdminInlineIngredientQuantityForm(forms.ModelForm):
    class Meta:
        model   = IngredientQuantity
        fields  = '__all__'
        # Reduce the width on the measure field.
        widgets = {
            'measure': TextInput(attrs={'size': '5'}),
        }
    pass

class AdminInlineRecipeSection(admin.TabularInline):
    extra = 0
    model = RecipeSection

class AdminInlineRecipeEquipment(admin.TabularInline):
    extra = 0
    model = RecipeEquipment

class AdminInlineIngredientQuantity(admin.TabularInline):
    extra = 0
    model = IngredientQuantity
    form  = AdminInlineIngredientQuantityForm

class AdminInlineRecipeStep(admin.TabularInline):
    extra = 0
    model = RecipeStep

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

@admin.register(RecipeTag)
class AdminRecipeTag(admin.ModelAdmin):
    pass
    
@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    inlines = [
        AdminInlineRecipeSection,
        AdminInlineRecipeEquipment,
        AdminInlineIngredientQuantity,
        AdminInlineRecipeStep,
    ]


