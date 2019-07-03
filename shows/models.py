from django.db import models
from music.models import Artist, Genre


class Show(models.Model):
    artists = models.ManyToManyField(Artist)
    genres = models.ManyToManyField(Genre, blank=True)

    date = models.DateField()
    time = models.TimeField(default="08:00")
    suggested_donation = models.IntegerField(default=7)

    facebook = models.URLField(default='', blank=True)

    def __str__(self):
        display = self.date.__str__() + ":"
        for artist in self.artists.all():
            display += artist.__str__() + "/"
        return display
