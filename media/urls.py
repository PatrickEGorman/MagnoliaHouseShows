from django.urls import path
from .views import fliers, photos, videos

urlpatterns = [
    path('fliers', fliers),
    path('photos', photos),
    path('videos', videos),
]