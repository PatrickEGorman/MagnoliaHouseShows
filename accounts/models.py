from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    @property
    def name(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        elif self.first_name:
            return self.first_name
        else:
            return self.username
