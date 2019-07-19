from django.db import models

from main.models import MetaData
from main.util import priority_choices, parse_date_string


class Genre(models.Model):
    name = models.TextField(unique=True, max_length=20)

    priority = models.IntegerField(choices=priority_choices, default=3)

    class Meta:
        ordering = ["priority", "name"]

    def __str__(self):
        return self.name

    metaData = models.OneToOneField(MetaData, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if self.metaData:
            self.metaData.save()
        else:
            meta = MetaData(name="Genre %s" % self.name)
            self.metaData = meta
        super(Genre, self).save(*args, **kwargs)


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

    priority = models.IntegerField(choices=priority_choices, default=3)

    class Meta:
        ordering = ["priority", "metadata__posted_on", "name"]

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genres.all()[:5])

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.name

    metaData = models.OneToOneField(MetaData, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if self.metaData:
            self.metaData.save()
        else:
            meta = MetaData(name="Artist %s" % self.name)
            self.metaData = meta
        super(Artist, self).save(*args, **kwargs)


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

    priority = models.IntegerField(choices=priority_choices, default=3)

    @property
    def release_date_string(self):
        return parse_date_string(self.release_date)

    class Meta:
        ordering = ["priority", "artist", "name"]

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genres.all()[:5])

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.name

    metaData = models.OneToOneField(MetaData, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if self.metaData:
            self.metaData.save()
        else:
            meta = MetaData(name="Album %s" % self.name)
            self.metaData = meta
        super(Album, self).save(*args, **kwargs)
