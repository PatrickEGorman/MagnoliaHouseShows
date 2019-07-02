from django.urls import path
from .views import music, view_album, view_band

urlpatterns = [
    path('', music),
    path('view_album', view_album),
    path('view_band', view_band),
]