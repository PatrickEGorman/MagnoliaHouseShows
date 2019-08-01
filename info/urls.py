from django.urls import path
from .views import show_about, list_directions, history_list, list_contacts, view_history, CreateHistory

urlpatterns = [
    path('about', show_about),
    path('directions', list_directions),
    path('history', history_list, name='history'),
    path("history/<history_id>", view_history),
    path('contact', list_contacts),
    path('submit_history', CreateHistory.as_view())
]