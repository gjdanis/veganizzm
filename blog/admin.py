from django.contrib import admin
from blog.models    import Post

# Admin configuration for the `blog` application. 
# `Post` is the only editable model on admin.

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    # The `slug` should be auto generated from the backend.
    exclude = ['slug',]