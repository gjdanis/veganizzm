from django.db                import models
from django.core.urlresolvers import reverse
from veganizzm.utilities      import generate_slug
from recipe.models import Recipe

# == `Post` ==
class Post(models.Model):
    # Represents a veganizzm blog post.
    class Meta:
        ordering = ['-date_created']

    title = models.CharField(max_length=100)
    slug  = models.SlugField(max_length=100, unique=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    published    = models.BooleanField(default=True)

    # A `Post` need not reference a `Recipe`.
    recipe  = models.OneToOneField(Recipe, null=True, blank=True, on_delete=models.PROTECT)
    
    # Override the `save` function to auto generate the `slug` field.
    def save(self, *args, **kwargs):
        self.slug = generate_slug(Post, self.title)
        return super(Post, self).save(*args, **kwargs)

    # Override the `get_absolute_url` to provide a preview link on the admin page.
    def get_absolute_url(self):
        return reverse('post_view', kwargs={'slug': self.slug})

    def __str__(self):
        return '{0} {1}'.format(self.date_created.date(), self.title)