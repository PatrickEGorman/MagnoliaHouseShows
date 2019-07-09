from django.db import models
from music.models import Artist, Genre


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

    class Meta:
        ordering = ["-date"]

    def display_artists(self):
        return '/ '.join(artist.name for artist in self.artists.all()[:5])
    display_artists.short_description = 'Artists'

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genres.all()[:5])
    display_genre.short_description = 'Genre'

    def save(self, *args, **kwargs):
        super(Show, self).save(*args, **kwargs)
        for artist in self.artists.all():
            for genre in artist.genres.all():
                self.genres.add(genre)
        super(Show, self).save(*args, **kwargs)

    def __str__(self):
        display = self.date.__str__() + ":"
        for artist in self.artists.all():
            display += artist.__str__() + "/"
        return display[:-1]
