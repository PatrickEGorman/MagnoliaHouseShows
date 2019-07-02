from django.db import models
from music.models import Band
from shows.models import Show


class Flier(models.Model):
    image = models.ImageField()
    date = models.DateField(blank=True, null=True, default=None)
    caption = models.TextField(default='', blank=True)
    show = models.ForeignKey(Show, null=True, blank=True, related_name="fliers", on_delete=models.SET_NULL)

    def __str__(self):
        if self.show:
            return "Flier for "+self.show
        elif "Flier from "+self.date:
            return self.date
        elif "Flier caption "+self.caption:
            return self.caption
        else:
            return "Database id for flier "+self.id


class Photo(models.Model):
    image = models.ImageField()
    date = models.DateField(blank=True, null=True, default=None)
    caption = models.TextField(default='', blank=True)
    band = models.ForeignKey(Band, null=True, blank=True, related_name="photos", on_delete=models.SET_NULL)
    show = models.ForeignKey(Show, null=True, blank=True, related_name="photos", on_delete=models.SET_NULL)

    def __str__(self):
        if self.band:
            return "Image of the band: "+self.band.__str__()
        elif self.show:
            return "Image from "+self.show.__str__()
        elif self.caption:
            return "Image caption "+self.caption
        else:
            return "Image database id "+str(self.id)


class YoutubeVideo(models.Model):
    youtube_url = models.URLField()
    date = models.DateField(blank=True, null=True, default=None)
    caption = models.TextField(default='', blank=True)
    bands = models.ManyToManyField(Band, blank=True)
    show = models.ForeignKey(Show, null=True, blank=True, related_name="videos", on_delete=models.SET_NULL)

    def __str__(self):
        if len(self.bands) == 1:
            return "Video of the band: "+self.bands[0].__str__()
        elif self.show:
            return "Image from "+self.show.__str__()
        elif self.caption:
            return "Image caption "+self.caption
        else:
            return "Image database id "+str(self.id)