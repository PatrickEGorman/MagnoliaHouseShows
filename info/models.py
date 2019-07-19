from django.db import models

import datetime

from main.models import MetaData
from main.util import priority_choices, parse_date_string
from media.models import Flier, Photo, YoutubeVideo
from music.models import Artist
from shows.models import Show


class InfoPage(models.Model):
    page_name = models.TextField(choices=[("about", "About"), ("contact", "Contact")], default="about")
    image = models.ImageField(blank=True, null=True)
    image_caption = models.TextField(blank=True, null=True)
    title = models.TextField(default='')
    text = models.TextField(default='')

    priority = models.IntegerField(choices=priority_choices, default=3)

    class Meta:
        ordering = ["priority", "metaData__posted_on", "title"]

    def __str__(self):
        return "Page:%s Title %s"%(self.page_name, self.title)

    metaData = models.OneToOneField(MetaData, on_delete=models.SET_NULL, null=True)

    def __init__(self, *args, **kwargs):
        super(InfoPage, self).__init__(*args, **kwargs)
        if not self.metaData:
            meta = MetaData()
            self.metaData = meta

    def save(self, *args, **kwargs):
        self.metaData.set_name(name="Info page category %s title %s" % (self.page_name, self.title))
        self.metaData.save()
        self.metaData = MetaData.objects.get(pk=self.metaData.pk)
        super(InfoPage, self).save(*args, **kwargs)


class History(InfoPage):
    artists = models.ManyToManyField(Artist, blank=True)
    shows = models.ManyToManyField(Show, blank=True)
    flier = models.ForeignKey(Flier, blank=True, null=True, on_delete=models.SET_NULL)
    photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL)
    youtube_video = models.ForeignKey(YoutubeVideo, blank=True, null=True, on_delete=models.SET_NULL)
    start_or_primary_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    approximate_date = models.BooleanField()

    def __init__(self, *args, **kwargs):
        super(History, self).__init__(*args, **kwargs)
        self.page_name = "History"

    @property
    def start_year_month(self):
        return parse_date_string(self.start_or_primary_date, year_month=True)

    @property
    def start_date_string(self):
        return parse_date_string(self.start_or_primary_date)

    @property
    def end_year_month(self):
        return parse_date_string(self.end_date, year_month=True)

    @property
    def end_date_string(self):
        return parse_date_string(self.end_date)

    @property
    def has_end(self):
        if self.end_date:
            return True


class Directions(InfoPage):
    starting_point = models.TextField(default='', blank=True)

    def __init__(self, *args, **kwargs):
        super(Directions, self).__init__(*args, **kwargs)
        self.page_name = "Directions"

    def __str__(self):
        if self.starting_point:
            return "Directions from %s" % self.starting_point
        else:
            return super(Directions, self).__str__()
