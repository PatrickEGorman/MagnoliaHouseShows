from django.db import models

from main.models import MetaData
from music.models import Artist, Genre
from main.util import priority_choices, parse_date_string


class Show(models.Model):
    artists = models.ManyToManyField(Artist)

    date = models.DateField()
    time = models.TimeField(default="08:00")
    suggested_donation = models.IntegerField(default=7)
    suggested_donation_max = models.IntegerField(blank=True, null=True)

    facebook = models.URLField(default='', blank=True)
    instagram = models.URLField(default='', blank=True)

    description = models.TextField(default='', blank=True)

    priority = models.IntegerField(choices=priority_choices, default=3)

    @property
    def genres(self):
        genre_name_list = {}
        for artist in self.artists.all():
            for genre in artist.genres.all():
                if not genre.name in genre_name_list:
                    genre_name_list[genre.name] = {'count': 1, 'priority': genre.priority}
                else:
                    genre_name_list[genre.name]['count'] += 1
        return genre_name_list

    @property
    def sorted_genres(self):
        sorted = []
        genres = self.genres
        for genre in genres:
            is_inserted = False
            if not sorted:
                sorted.append(genre)
                continue
            for x in range(len(sorted)):
                if genres[genre]['count'] > genres[sorted[x]]['count']:
                    sorted.insert(x-1, genre)
                    is_inserted = True
                    break
                elif genres[genre]['count'] == genres[sorted[x]]['count']:
                    if genres[genre]['priority'] >= genres[sorted[x]]['priority']:
                        sorted.insert(x-1, genre)
                        is_inserted = True
                        break
            if not is_inserted:
                sorted.append(genre)
        return sorted

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
        return ', '.join(genre for genre in self.sorted_genres[:5])
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
        try:
            if not self.genres:
                for artist in Artist.objects.filter(show__id=self.id):
                    for genre in artist.genres.all():
                        self.genres.add(genre)
                self.save()
        except ValueError:
            print("Show not initialized")

    def save(self, *args, **kwargs):
        self.metaData.set_name(name="Show for %s" % (self.__str__()))
        self.metaData.save()
        self.metaData = MetaData.objects.get(pk=self.metaData.pk)
        super(Show, self).save(*args, **kwargs)

