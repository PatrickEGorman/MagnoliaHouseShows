from django.urls import path
from .views import about, directions, history, contact

urlpatterns = [
    path('about', about),
    path('directions', directions),
    path('history', history),
    path('contact', contact),
]