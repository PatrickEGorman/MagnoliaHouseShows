from accounts.views import SignUp
from django.urls import path

urlpatterns = [
    path('create_account', Signup.as_view()),
    path('authenticate_facebook', view_show),
]
