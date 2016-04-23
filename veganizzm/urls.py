"""veganizzm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^$", "blog.views.home", name="home"),
    url(r"^post/manage/$", "blog.views.post_management", name="post_management"),
    url(r"^recipe/manage/$", "recipe.views.recipe_management", name="recipe_management"),
    url(r"^ajax/post/preview/$", "blog.views.post_preview", name="post_preview"),
    url(r"^ajax/recipe/preview/$", "recipe.views.recipe_preview", name="recipe_preview"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
