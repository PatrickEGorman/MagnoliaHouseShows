from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    permission_to_contact = models.BooleanField(default=False, blank=True)

    @property
    def name(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        elif self.first_name:
            return self.first_name
        else:
            return self.username
