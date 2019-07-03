from django.db import models


class Genre(models.Model):
    name = models.TextField(unique=True)
    sub_genres = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.TextField()
    hometown = models.TextField(default='', blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    bandcamp = models.URLField(default='', blank=True)
    youtube = models.URLField(default='', blank=True)
    facebook = models.URLField(default='', blank=True)
    soundcloud = models.URLField(default='', blank=True)

    def __str__(self):
        return "Band "+self.name


class Album(models.Model):
    name = models.TextField()
    artist = models.ForeignKey(Artist, null=True, blank=True, related_name='albums', on_delete=models.SET_NULL)
    cover_image = models.ImageField(blank=True)
    bandcamp = models.URLField(default='', blank=True)
    youtube = models.URLField(default='', blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    release_date = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return "Album "+self.name

class Song(models.Model):
    name = models.TextField()
    genres = models.ManyToManyField(Genre, blank=True)
    album = models.ForeignKey(Album, null=True, blank=True, related_name='songs', on_delete=models.SET_NULL)

    def __str__(self):
        return "Song " + self.name
