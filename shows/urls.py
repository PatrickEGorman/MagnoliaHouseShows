from django.urls import path
from .views import shows, view_show, get_shows_list

urlpatterns = [
    path('', shows),
    path('view_show', view_show),
    path('list_shows', get_shows_list)
]