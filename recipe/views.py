from django.shortcuts import render, get_object_or_404
from recipe.models    import Recipe

# == `recipe_view` == 
def recipe_view(request, slug):
    # View a `Recipe` by `slug`. It might
    # be a good idea to restrict this view to staff.

    recipe = get_object_or_404(Recipe, slug=slug)
    data = {
        'recipe': recipe,
        'ingredient_quantities': recipe.ingredient_quantity_set.all(),
        'unordered_steps': [
            recipe_step for recipe_step in recipe.recipe_step_set.all() 
                        if  recipe_step.number is None
        ],
        'ordered_recipe_steps': [
            recipe_step for recipe_step in recipe.recipe_step_set.all() 
                        if  recipe_step.number is not None
        ]
    }
    return render(request, 'recipe_template.html', data)