"""MagnoliaHouseShows URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.main, name='main')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='main')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from main.views import home


class FaviconView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        self.url = '/static/images/favicon/%s.%s' % (kwargs['file_name'], kwargs['file_format'])
        self.permanent = True
        return super().get_redirect_url(*args, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('<file_name>.<file_format>', FaviconView.as_view()),
    path('shows/', include('shows.urls')),
    path('music/', include('music.urls')),
    path('info/', include('info.urls')),
    path('media/', include('media.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include('accounts.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
]

if settings.MEDIA_URL == "/uploads/":
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
