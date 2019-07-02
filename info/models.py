from django.db import models


class InfoPage(models.Model):
    image = models.ImageField(blank=True, null=True)
    image_caption = models.TextField(blank=True, null=True)
    title = models.TextField(default='', blank=True)
    text = models.TextField(default='')


class Directions(InfoPage):
    starting_point = models.TextField(default='', blank=True)
