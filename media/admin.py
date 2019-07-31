from django.contrib import admin

from main.admin import meta_created_date, meta_created_by, ModelAdminWithMeta
from .models import Flier, Photo, YoutubeVideo


class FlierAdmin(ModelAdminWithMeta):
    list_display = ('show', 'priority', 'image', 'date', meta_created_date, meta_created_by)
    list_filter = ('date', 'priority',  'show')
    fields = ('show', 'priority', 'image', 'caption', 'date')


class PhotoAdmin(ModelAdminWithMeta):
    list_display = ('image', 'priority', 'caption', 'artist', 'show', 'date', meta_created_date, meta_created_by)
    list_filter = ('date', 'priority', 'artist', 'show')
    fields = ('artist', 'priority', 'image', 'caption', 'date')


class YoutubeAdmin(ModelAdminWithMeta):
    list_display = ('caption', 'priority', 'youtube_url', 'artist', 'show', 'date', meta_created_date,
                    meta_created_by)
    list_filter = ('date', 'priority', 'artist', 'show')
    fields = (('artist', 'show'), 'youtube_url', 'priority', 'caption', 'date')


admin.site.register(Flier, FlierAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(YoutubeVideo, YoutubeAdmin)
