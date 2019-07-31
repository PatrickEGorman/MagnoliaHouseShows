from django.urls import path
from .views import show_about, list_directions, history_list, list_contacts, view_history

urlpatterns = [
    path('about', show_about),
    path('directions', list_directions),
    path('history', history_list),
    path("history/<history_id>", view_history),
    path('contact', list_contacts),
]