from django.views.generic import DetailView
from recipe.models import Recipe

# == `RecipeView` ==
class RecipeView(DetailView):
    # View for a single `Recipe` object. The instructions of 
    # a `Recipe` are only numbered if there is more than one instruction.
    template_name = 'recipe_template.html'
    model = Recipe

    def get_context_data(self, *args, **kwargs):
        context = super(RecipeView, self).get_context_data(*args, **kwargs)
        context['number_steps'] = len(context['object'].recipe_step_set.all()) > 1
        return context