from django.db import models
from music.models import Band, Genre


class Show(models.Model):
    bands = models.ManyToManyField(Band)
    genres = models.ManyToManyField(Genre, blank=True)

    date = models.DateField()
    time = models.TimeField(default="08:00")
    suggested_donation = models.IntegerField(default=7)

    facebook = models.URLField(default='', blank=True)

    def __str__(self):
        display = self.date.__str__() + ":"
        for band in self.bands.all():
            display += band + "/"
        return display
