from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from main.models import MetaData
from main.util import priority_choices, parse_date_string
from music.models import Artist
from shows.models import Show


class Flier(models.Model):
    image = models.ImageField()
    date = models.DateField(default=None)
    caption = models.TextField(default='', blank=True)
    show = models.OneToOneField(Show, null=True, blank=True, related_name="flier", on_delete=models.SET_NULL)

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

    def __init__(self, *args, **kwargs):
        super(Flier, self).__init__(*args, **kwargs)
        if not self.metaData:
            meta = MetaData()
            self.metaData = meta

    metaData = models.OneToOneField(MetaData, on_delete=models.SET_NULL, null=True)

    def __init__(self, *args, **kwargs):
        super(Flier, self).__init__(*args, **kwargs)
        if not self.metaData:
            meta = MetaData()
            self.metaData = meta

    def save(self, *args, **kwargs):
        self.metaData.set_name(name=self.__str__())
        self.metaData.save()
        self.metaData = MetaData.objects.get(pk=self.metaData.pk)
        super(Flier, self).save(*args, **kwargs)


class Photo(models.Model):
    image = models.ImageField()
    date = models.DateField(blank=True, null=True, default=None)
    caption = models.CharField(default='', blank=True, max_length=250)
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

    def __init__(self, *args, **kwargs):
        super(Photo, self).__init__(*args, **kwargs)
        if not self.metaData:
            meta = MetaData()
            self.metaData = meta

    metaData = models.OneToOneField(MetaData, on_delete=models.SET_NULL, null=True)

    def __init__(self, *args, **kwargs):
        super(Photo, self).__init__(*args, **kwargs)
        if not self.metaData:
            meta = MetaData()
            self.metaData = meta

    def save(self, *args, **kwargs):
        self.metaData.set_name(name=self.__str__())
        self.metaData.save()
        self.metaData = MetaData.objects.get(pk=self.metaData.pk)
        super(Photo, self).save(*args, **kwargs)


def validate_youtube_url(url):
    if "youtu" not in url:
        raise ValidationError(
            _("%(url)s is not a valid youtube url"),
            params={'url': url}
        )


class YoutubeVideo(models.Model):
    youtube_url = models.URLField(validators=[validate_youtube_url])
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

    @property
    def embed_url(self):
        url_ender = self.youtube_url.split('/')[:-1]
        url_ender = url_ender.split('=')[:-1]
        return "https://www.youtube.com/embed/"+url_ender

    class Meta:
        ordering = ["priority", "-metaData__posted_on", "show", "artist"]

    def __str__(self):
        if self.artist:
            return "Video of the band: "+self.artist.__str__()
        elif self.show:
            return "Video from: "+self.show.__str__()
        elif self.caption:
            return "Video caption: "+self.caption
        else:
            return "Video url: "+self.youtube_url

    def __init__(self, *args, **kwargs):
        super(YoutubeVideo, self).__init__(*args, **kwargs)
        if not self.metaData:
            meta = MetaData()
            self.metaData = meta

    metaData = models.OneToOneField(MetaData, on_delete=models.SET_NULL, null=True)

    def __init__(self, *args, **kwargs):
        super(YoutubeVideo, self).__init__(*args, **kwargs)
        if not self.metaData:
            meta = MetaData()
            self.metaData = meta

    def save(self, *args, **kwargs):
        self.metaData.set_name(name=self.__str__())
        self.metaData.save()
        self.metaData = MetaData.objects.get(pk=self.metaData.pk)
        super(YoutubeVideo, self).save(*args, **kwargs)
