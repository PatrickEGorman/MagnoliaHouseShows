from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(_('email address'), blank=True, unique=True)
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')
    can_upload = models.BooleanField(default=False)


class FacebookUser(User):
    password = None
    facebook_id = models.TextField(unique=True)
