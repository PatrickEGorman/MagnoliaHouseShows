from django.db import models


class Genre(models.Model):
    name = models.TextField(unique=True)
    sub_genres = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.TextField()
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return "Song "+self.name


class Album(models.Model):
    name = models.TextField()
    cover_image = models.ImageField(blank=True)
    bandcamp = models.URLField(default='', blank=True)
    youtube = models.URLField(default='', blank=True)
    songs = models.ManyToManyField(Song, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    release_date = models.DateField(blank=True, null=True, default=None)

    def __str__(self):
        return "Album "+self.name


class Band(models.Model):
    name = models.TextField()
    albums = models.ManyToManyField(Album, blank=True)
    hometown = models.TextField(default='', blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    bandcamp = models.URLField(default='', blank=True)
    youtube = models.URLField(default='', blank=True)
    facebook = models.URLField(default='', blank=True)
    soundcloud = models.URLField(default='', blank=True)

    def __str__(self):
        return "Band "+self.name
