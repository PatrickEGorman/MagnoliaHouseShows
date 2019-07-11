from django.db import models


class Genre(models.Model):
    name = models.TextField(unique=True, max_length=20)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.TextField()
    hometown = models.TextField(default='', blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    bandcamp = models.URLField(default='', blank=True)
    bandcamp_embed_code = models.TextField(default='', blank=True)
    soundcloud_embed_code = models.TextField(default='', blank=True)
    youtube_embed_code = models.TextField(default='', blank=True)
    youtube = models.URLField(default='', blank=True)
    facebook = models.URLField(default='', blank=True)
    soundcloud = models.URLField(default='', blank=True)
    description = models.TextField(default='', blank=True)

    class Meta:
        ordering = ["name"]

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genres.all()[:5])

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.TextField()
    artist = models.ForeignKey(Artist, null=True, blank=True, related_name='albums', on_delete=models.SET_NULL)
    cover_image = models.ImageField(blank=True)
    bandcamp_embed_code = models.TextField(default='', blank=True)
    youtube_embed_code = models.TextField(default='', blank=True)
    bandcamp = models.URLField(default='', blank=True)
    youtube = models.URLField(default='', blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    release_date = models.DateField(blank=True, null=True, default=None)
    description = models.TextField(default='', blank=True)

    class Meta:
        ordering = ["artist", "name"]

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genres.all()[:5])

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.name
