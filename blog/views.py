from django.views.generic import DetailView
from blog.models import Post

# == `PostView` ==
class PostView(DetailView):
    # View a `Post` by `slug`.
    template_name = 'post_template.html'
    model = Post