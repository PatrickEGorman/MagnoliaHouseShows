from django.urls import path
from .views import fliers, photos, videos, get_fliers_list, get_photos_list, get_videos_list, SubmitPhoto, SubmitVideo

urlpatterns = [
    path('fliers', fliers),
    path('photos', photos, name="photos"),
    path('videos', videos, name="videos"),
    path('list_fliers', get_fliers_list),
    path('list_photos', get_photos_list),
    path('list_videos', get_videos_list),
    path('submit_photo', SubmitPhoto.as_view()),
    path('submit_video', SubmitVideo.as_view()),
]