from django.urls import path
from .views import about, directions, event_calendar, history

urlpatterns = [
    path('about', about),
    path('directions', directions),
    path('event_calendar', event_calendar),
    path('history', history),
]