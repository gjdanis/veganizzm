from django.contrib import admin
from recipe.models  import Recipe, RecipeStep, Ingredient, IngredientQuantity

# Admin configuration for the `recipe` application. 
# Only `Recipe` and `Ingredient` are editable on admin. `RecipeStep`
# and `IngredientQuantity` should be created or modified inline
# from a `Recipe`.

class InlineIngredientQuantity(admin.TabularInline):
    extra = 0
    model = IngredientQuantity

class InlineRecipeStep(admin.TabularInline):
    extra = 0
    model = RecipeStep
    inlines = [InlineIngredientQuantity]
    
@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    # The `slug` should be auto generated from the backend.
    exclude = ['slug',]
    inlines = [InlineIngredientQuantity, InlineRecipeStep,]

@admin.register(Ingredient)
class AdminIngredient(admin.ModelAdmin):
    pass
