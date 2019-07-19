from django.contrib import admin

from main.admin import meta_created_date, meta_created_by, ModelAdminWithMeta
from .models import Flier, Photo, YoutubeVideo


class FlierAdmin(ModelAdminWithMeta):
    list_display = ('show', 'priority', 'image', 'date', meta_created_date, meta_created_by)
    list_filter = ('date', 'priority',  'show')


class PhotoAdmin(ModelAdminWithMeta):
    list_display = ('image', 'priority', 'caption', 'artist', 'show', 'date', meta_created_date, meta_created_by)
    list_filter = ('date', 'priority', 'artist', 'show')


class YoutubeAdmin(ModelAdminWithMeta):
    list_display = ('caption', 'priority', 'youtube_url', 'artist', 'show', 'date', meta_created_date,
                    meta_created_by)
    list_filter = ('date', 'priority', 'artist', 'show')


admin.site.register(Flier, FlierAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(YoutubeVideo, YoutubeAdmin)
