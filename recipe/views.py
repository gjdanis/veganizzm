from django.shortcuts import render, get_object_or_404
from recipe.models    import Recipe

# == `recipe_view` == 
def recipe_view(request, slug):
    # View a `Recipe` by `slug`. It might
    # be a good idea to restrict this view to staff.
    
    recipe = get_object_or_404(Recipe, slug=slug)
    return render(request, 'recipe_view.html')