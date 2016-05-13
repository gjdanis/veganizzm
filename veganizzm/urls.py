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
from django.contrib   import admin
from django.conf      import settings
from django.conf.urls.static import static

import blog.views
import recipe.views

urlpatterns = [
    url(r'^redactor/', include('redactor.urls')),
    url(r'^$', blog.views.home_view),
    url(r'^admin/', admin.site.urls),
    url(r'^posts/(?P<slug>[-\w\d\_]+)/$', blog.views.post_view, name='post_view'),
    url(r'^recipes/(?P<slug>[-\w\d\_]+)/$', recipe.views.recipe_view, name='recipe_view'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
