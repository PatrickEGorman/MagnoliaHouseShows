from django.urls import path
from .views import music, view_album, view_band, get_artist_list

urlpatterns = [
    path('', music),
    path('view_album', view_album),
    path('view_band', view_band),
    path('artist_list', get_artist_list)
]