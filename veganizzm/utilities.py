from django.template.defaultfilters import slugify

# File for common functions and classes. Business specific logic should
# be written at the application level. 

def generate_slug(cls, value):
    # Returns a unique human readable url string, generated from `value`.
    # Here, `cls` should be the model where `slug` is defined.
    
    count = 1
    slug = slugify(value)
    if not isinstance(cls, type):
        cls = cls.__class__

    def _get_query(cls, **kwargs):
        if cls.objects.filter(**kwargs).count():
            return True

    while _get_query(cls, slug=slug):
        slug = slugify(u'{0}-{1}'.format(value, count))
        while len(slug) > cls._meta.get_field('slug').max_length:
            value = value[:-1]
            slug = slugify(u'{0}-{1}'.format(value, count))
        count = count + 1
    return slug