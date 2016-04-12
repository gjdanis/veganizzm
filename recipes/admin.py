from django.contrib import admin
from recipes.models import Ingredient, IngredientQuantity, RecipeStep, Recipe

@admin.register(Ingredient)
class AdminIngredient(admin.ModelAdmin):
    pass

@admin.register(IngredientQuantity)
class AdminIngredientQuantity(admin.ModelAdmin):
    pass

@admin.register(RecipeStep)
class AdminRecipeStep(admin.ModelAdmin):
    pass

@admin.register(Recipe)
class AdminRecipe(admin.ModelAdmin):
    pass
