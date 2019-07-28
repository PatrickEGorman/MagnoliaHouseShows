from django.urls import path
from .views import music, view_album, view_artist, get_artist_list, get_artist

urlpatterns = [
    path('', music),
    path('view_album', view_album),
    path('artist/<artist_id>', view_artist),
    path('get_artist/<artist_id>', get_artist),
    path('artist_list', get_artist_list)
]