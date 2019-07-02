from accounts.views import SignUp, authenticate_facebook
from django.urls import path

urlpatterns = [
    path('create_account', SignUp.as_view()),
    path('authenticate_facebook', authenticate_facebook),
]
