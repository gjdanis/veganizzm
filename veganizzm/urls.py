"""
veganizzm site URL configuration. The `urlpatterns` routes URLs to views. 
For more information please see here: https://docs.djangoproject.com/en/1.9/topics/http/urls/

Function views
--
1. Add an import: `from my_app import views`
2. Add a URL to urlpatterns: 
    `url(r'^$', views.home, name='home')`

Class-based views
--
1. Add an import: `from other_app.views import Home`
2. Add a URL to urlpatterns: 
    `url(r'^$', Home.as_view(), name='home')`

Including another URL conf
--
1. Import the include() function: 
    `from django.conf.urls import url, include`
2. Add a URL to urlpatterns: 
    `url(r'^blog/', include('blog.urls'))`
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from recipe.views import RecipeDetailView, RecipeListView
from blog.views import PostView

urlpatterns = [
    url(r'^redactor/', include('redactor.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/(?P<slug>[-\w\d\_]+)/$', PostView.as_view(), name='post_view'),
    url(r'^recipes/list/', RecipeListView.as_view()),
    url(r'^recipes/(?P<slug>[-\w\d\_]+)/$', RecipeDetailView.as_view(), name='recipe_view')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
