from django.db import models
from music.models import Band
from shows.models import Show


class Flier(models.Model):
    image = models.ImageField()
    show = models.ForeignKey(Show, null=True, blank=True, related_name="fliers", on_delete=models.SET_NULL)


class Photo(models.Model):
    image = models.ImageField()
    caption = models.TextField(default='')
    band = models.ForeignKey(Band, null=True, blank=True, related_name="photos", on_delete=models.SET_NULL)
    show = models.ForeignKey(Show, null=True, blank=True, related_name="photos", on_delete=models.SET_NULL)


class YoutubeVideo(models.Model):
    youtube_url = models.TextField()
    caption = models.TextField(default='')
    bands = models.ManyToManyField(Band, blank=True)
    show = models.ForeignKey(Show, null=True, blank=True, related_name="videos", on_delete=models.SET_NULL)
