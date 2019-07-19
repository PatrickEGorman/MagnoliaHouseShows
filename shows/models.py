from django.db import models

from main.models import MetaData
from music.models import Artist, Genre
from main.util import priority_choices, parse_date_string


class Show(models.Model):
    artists = models.ManyToManyField(Artist)
    genres = models.ManyToManyField(Genre, blank=True)

    date = models.DateField()
    time = models.TimeField(default="08:00")
    suggested_donation = models.IntegerField(default=7)
    suggested_donation_max = models.IntegerField(blank=True, null=True)

    facebook = models.URLField(default='', blank=True)
    instagram = models.URLField(default='', blank=True)

    description = models.TextField(default='', blank=True)

    priority = models.IntegerField(choices=priority_choices, default=3)

    @property
    def year_month(self):
        return parse_date_string(self.date, year_month=True)

    @property
    def date_string(self):
        return parse_date_string(self.date)

    class Meta:
        ordering = ["priority", "-date"]

    def display_artists(self):
        return '/ '.join(artist.name for artist in self.artists.all()[:5])
    display_artists.short_description = 'Artists'

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genres.all()[:5])
    display_genre.short_description = 'Genre'

    def __str__(self):
        display = self.date.__str__() + ":"
        for artist in self.artists.all():
            display += artist.__str__() + "/"
        return display[:-1]

    metaData = models.OneToOneField(MetaData, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        super(Show, self).save(*args, **kwargs)
        for artist in self.artists.all():
            for genre in artist.genres.all():
                self.genres.add(genre)
        super(Show, self).save(*args, **kwargs)

        if self.metaData:
            self.metaData.save()
        else:
            meta = MetaData(name="Show for %s %s" % (self.date.__str__(), self.display_artists))
            self.metaData = meta
        super(Show, self).save(*args, **kwargs)
