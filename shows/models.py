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
        return '/ '.join(artist.name for artist in Artist.objects.filter(show__id=self.id)[:5])
    display_artists.short_description = 'Artists'

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genres.all()[:5])
    display_genre.short_description = 'Genre'

    def __str__(self):
        display = self.date.__str__() + ":"
        for artist in Artist.objects.filter(show__id=self.id):
            display += artist.__str__() + "/"
        return display[:-1]

    metaData = models.OneToOneField(MetaData, on_delete=models.SET_NULL, null=True)

    def __init__(self, *args, **kwargs):
        super(Show, self).__init__(*args, **kwargs)
        if not self.metaData:
            meta = MetaData()
            self.metaData = meta

    def save(self, *args, **kwargs):
        self.metaData.set_name(name="Show %s" % self.__str__())
        self.metaData.save()
        self.metaData = MetaData.objects.get(pk=self.metaData.pk)
        super(Show, self).save(*args, **kwargs)
