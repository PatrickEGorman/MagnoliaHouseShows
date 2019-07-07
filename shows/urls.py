from django.urls import path
from .views import past_shows, view_show, get_show, get_shows_list

urlpatterns = [
    path('past', past_shows),
    path('view_show/<show_id>', view_show),
    path('get_show/<show_id>', get_show),
    path('list_shows', get_shows_list)
]