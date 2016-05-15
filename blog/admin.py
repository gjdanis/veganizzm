from django.contrib        import admin
from django                import forms
from blog.models           import Post
from django.forms          import TextInput
from redactor.widgets      import RedactorEditor
from taggit_labels.widgets import LabelWidget

# Admin configuration for the `blog` application. 
# `Post` is the only editable model on admin.

class AdminPostForm(forms.ModelForm):
    # This form should eventually allow editing the `content`
    # field from a rich text box.
    class Meta:
        model  = Post
        fields = '__all__'
        widgets = {
            'content': RedactorEditor(),
            'tags': LabelWidget()
        }
    pass

@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    # The `slug` should be auto generated from the backend.
    filter_horizontal = ['recipes',]
    list_display  = ['title', 'author']
    search_fields = ['title']
    list_per_page = 25
    form = AdminPostForm

    # Saves a `Post` and by default assigns the currently
    # logged in user as the `author`.
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
