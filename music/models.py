from django.db import models


class Genre(models.Model):
    name = models.TextField(unique=True, primary_key=True)
    sub_genres = models.ManyToManyField('self', blank=True)


class Song(models.Model):
    name = models.TextField()
    genres = models.ManyToManyField(Genre, blank=True)


class Album(models.Model):
    name = models.TextField()
    cover_image = models.ImageField(blank=True)
    band_camp = models.URLField(default='')
    youtube = models.URLField(default='')
    songs = models.ManyToManyField(Song, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)


class Band(models.Model):
    name = models.TextField()
    albums = models.ManyToManyField(Album, blank=True)
    home_town = models.TextField(default='')
    genres = models.ManyToManyField(Genre)
    band_camp = models.URLField(default='')
    youtube = models.URLField(default='')
    facebook = models.URLField(default='')
    soundcloud = models.URLField(default='')
