from django.urls import path
from .views import shows, view_show

urlpatterns = [
    path('', shows),
    path('view_show', view_show),
]