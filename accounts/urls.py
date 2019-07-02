from accounts.views import SignUp
from django.urls import path

urlpatterns = [
    path('create_account', SignUp.as_view()),
]
