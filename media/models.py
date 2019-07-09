from django.db import models
from music.models import Artist
from shows.models import Show


class Flier(models.Model):
    image = models.ImageField()
    caption = models.TextField(default='', blank=True)
    show = models.ForeignKey(Show, null=True, blank=True, related_name="fliers", on_delete=models.SET_NULL)
    date = models.DateField(default=show.date)


    def __str__(self):
        if self.show:
            return "Flier for: "+self.show.__str__()
        elif self.date:
            return "Flier from: "+self.date.__str__()
        elif self.caption:
            return "Flier caption: "+self.caption
        else:
            return "Database id for flier: "+str(self.id)


class Photo(models.Model):
    image = models.ImageField()
    caption = models.TextField(default='', blank=True)
    artist = models.ForeignKey(Artist, null=True, blank=True, related_name="photos", on_delete=models.SET_NULL)
    show = models.ForeignKey(Show, null=True, blank=True, related_name="photos", on_delete=models.SET_NULL)
    date = models.DateField(default=show.date)


    def __str__(self):
        if self.artist:
            return "Image of the band: "+self.artist.__str__()
        elif self.show:
            return "Image from: "+self.show.__str__()
        elif self.caption:
            return "Image caption: "+self.caption
        else:
            return "Image database id: "+str(self.id)


class YoutubeVideo(models.Model):
    youtube_url = models.URLField()
    caption = models.TextField(default='', blank=True)
    artist = models.ForeignKey(Artist, null=True, related_name='videos', on_delete=models.SET_NULL, blank=True)
    show = models.ForeignKey(Show, null=True, blank=True, related_name="videos", on_delete=models.SET_NULL)
    date = models.DateField(default=show.date)

    def __str__(self):
        if self.artist:
            return "Video of the band: "+self.artist.__str__()
        elif self.show:
            return "Image from: "+self.show.__str__()
        elif self.caption:
            return "Image caption: "+self.caption
        else:
            return "Image database id: "+str(self.id)