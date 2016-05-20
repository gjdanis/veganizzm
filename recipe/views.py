from django.views.generic import DetailView, ListView
from recipe.models import Recipe

# == `RecipeDetailView` ==
class RecipeDetailView(DetailView):
    # View for a single `Recipe` object. The instructions of 
    # a `Recipe` are only numbered if there is more than one instruction.
    template_name = 'recipe_template.html'
    model = Recipe

    def get_context_data(self, *args, **kwargs):
        context = super(RecipeDetailView, self).get_context_data(*args, **kwargs)
        context['number_steps'] = len(context['object'].recipe_step_set.all()) > 1
        return context

# == `RecipeListView` ==
class RecipeListView(ListView):
    template_name = 'recipe_list_template.html'
    model = Recipe
