from django.db import models

from main.models import MetaData
from main.util import priority_choices, parse_date_string
from music.models import Artist
from shows.models import Show


class Flier(models.Model):
    image = models.ImageField()
    date = models.DateField(default=None)
    caption = models.TextField(default='', blank=True)
    show = models.ForeignKey(Show, null=True, blank=True, related_name="fliers", on_delete=models.SET_NULL)

    priority = models.IntegerField(choices=priority_choices, default=3)

    @property
    def year_month(self):
        return parse_date_string(self.date, year_month=True)

    @property
    def date_string(self):
        return parse_date_string(self.date)

    class Meta:
        ordering = ["priority", "date", "show"]

    def __str__(self):
        if self.show:
            return "Flier for: "+self.show.__str__()
        elif self.date:
            return "Flier from: "+self.date.__str__()
        elif self.caption:
            return "Flier caption: "+self.caption
        else:
            return "Database id for flier: "+str(self.id)

    metaData = models.OneToOneField(MetaData, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if self.metaData:
            self.metaData.save()
        else:
            meta = MetaData(name="Flier for %s %s" % (self.date.__str__(), self.show))
            self.metaData = meta
        super(Flier, self).save(*args, **kwargs)


class Photo(models.Model):
    image = models.ImageField()
    date = models.DateField(blank=True, null=True, default=None)
    caption = models.TextField(default='', blank=True)
    artist = models.ForeignKey(Artist, null=True, blank=True, related_name="photos", on_delete=models.SET_NULL)
    show = models.ForeignKey(Show, null=True, blank=True, related_name="photos", on_delete=models.SET_NULL)

    priority = models.IntegerField(choices=priority_choices, default=3)

    @property
    def year_month(self):
        return parse_date_string(self.date, year_month=True)

    @property
    def date_string(self):
        return parse_date_string(self.date)

    class Meta:
        ordering = ["priority", "date", "show", "artist"]

    def __str__(self):
        if self.artist:
            return "Image of the band: "+self.artist.__str__()
        elif self.show:
            return "Image from: "+self.show.__str__()
        elif self.caption:
            return "Image caption: "+self.caption
        else:
            return "Image database id: "+str(self.id)

    metaData = models.OneToOneField(MetaData, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if self.metaData:
            self.metaData.save()
        else:
            meta = MetaData(name="Photo for %s %s %s" % (self.date.__str__(), self.artist, self.show))
            self.metaData = meta
        super(Photo, self).save(*args, **kwargs)


class YoutubeVideo(models.Model):
    youtube_url = models.URLField()
    date = models.DateField(blank=True, null=True, default=None)
    caption = models.TextField(default='', blank=True)
    artist = models.ForeignKey(Artist, null=True, related_name='videos', on_delete=models.SET_NULL, blank=True)
    show = models.ForeignKey(Show, null=True, blank=True, related_name="videos", on_delete=models.SET_NULL)

    priority = models.IntegerField(choices=priority_choices, default=3)

    @property
    def year_month(self):
        return parse_date_string(self.date, year_month=True)

    @property
    def date_string(self):
        return parse_date_string(self.date)

    class Meta:
        ordering = ["priority", "date", "show", "artist"]

    def __str__(self):
        if self.artist:
            return "Video of the band: "+self.artist.__str__()
        elif self.show:
            return "Image from: "+self.show.__str__()
        elif self.caption:
            return "Image caption: "+self.caption
        else:
            return "Image database id: "+str(self.id)

    metaData = models.OneToOneField(MetaData, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if self.metaData:
            self.metaData.save()
        else:
            meta = MetaData(name="Youtube video %s" % self.youtube_url)
            self.metaData = meta
        super(YoutubeVideo, self).save(*args, **kwargs)