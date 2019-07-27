from django.urls import path
from .views import about, directions, event_calendar, history, contact

urlpatterns = [
    path('about', about),
    path('directions', directions),
    path('history', history),
    path('contact', contact),
]