from django.shortcuts import render, get_object_or_404
from blog.models      import Post

# == `home` ==
def home_view(request):
    # Renders the home page.
    return render(request, 'index.html')

# == `post_view` == 
def post_view(request, slug):
    # View a `Post` by `slug`.
    
    post = get_object_or_404(Post, slug=slug)
    data = {'title': post.title, 'content': post.content}
    return render(request, 'post_view.html', data)