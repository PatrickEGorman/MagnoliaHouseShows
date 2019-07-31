from django.urls import path
from .views import about, directions, history_list, contact, view_history

urlpatterns = [
    path('about', about),
    path('directions', directions),
    path('history', history_list),
    path("history/<history_id>", view_history),
    path('contact', contact),
]