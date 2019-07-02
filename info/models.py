from django.db import models


class InfoPage(models.Model):
    image = models.ImageField(blank=True, null=True)
    text = models.TextField(default='')


class Directions(InfoPage):
    starting_point = models.TextField(default='', blank=True)
