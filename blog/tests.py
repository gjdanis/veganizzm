from django.test import TestCase
from blog.models import Post
from recipes.models import Recipe

class PostTests(TestCase):
    fixtures = ['sample-blog.json']

    def test_delete_recipe(self):
        pass

    def test_delete_post(self):
        pass