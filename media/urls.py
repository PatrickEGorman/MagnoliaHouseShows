from django.urls import path
from .views import fliers, photos, videos, get_fliers_list, get_photos_list, get_videos_list

urlpatterns = [
    path('fliers', fliers),
    path('photos', photos),
    path('videos', videos),
    path('list_fliers', get_fliers_list),
    path('list_photos', get_photos_list),
    path('list_videos', get_videos_list),
]