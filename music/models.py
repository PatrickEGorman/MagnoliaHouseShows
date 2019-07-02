from django.db import models


class Genre(models.Model):
    name = models.TextField(unique=True)
    sub_genres = models.ManyToManyField('self')


class Song(models.Model):
    name = models.TextField()
    genres = models.ManyToManyField(Genre, blank=True)


class Album(models.Model):
    name = models.TextField()
    cover_image = models.ImageField(blank=True)
    band_camp = models.URLField(default='')
    youtube = models.URLField(default='')
    songs = models.ManyToManyField(Song)
    genres = models.ManyToManyField(Genre)


class Band(models.Model):
    name = models.TextField()
    albums = models.ManyToManyField(Album)
    home_town = models.TextField(default='')
    genres = models.ManyToManyField(Genre)
    band_camp = models.URLField(default='')
    youtube = models.URLField(default='')
    facebook = models.URLField(default='')
    soundcloud = models.URLField(default='')
