from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import login

from accounts.forms import CustomUserCreationForm
from .models import FacebookUser


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def authenticate_facebook(request):
    if request.method == "POST":
        name = request.body['name']
        id = request.body['id']
        if FacebookUser.objects.filter(facebook_id=id):
            login(FacebookUser)
        else:
            split_name = name.split(" ")
            first = split_name[0]
            last = split_name[split_name.length - 1]
            user = FacebookUser()
            user.facebook_id = id
            user.first_name = first
            user.last_name = last
            user.username = name
            user.save()
