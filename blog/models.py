from django.db import models
from recipes.models import Recipe

class Post(models.Model):
    """
    Represents a Veganizzm blog/recipe post

    Attributes:
        title (str): title to display of the post
        recipe (Recipe|null): what the post is about (not all posts need have recipes)
        content (str): the raw content of the post
        date_created (date): when the post was created
        published (bool): whether or not the post is live
    """

    title = models.CharField(max_length=100)
    recipe = models.OneToOneField(Recipe, null=True, on_delete=models.PROTECT)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date_created"]


