from django.contrib import admin

from main.admin import meta_created_date, meta_created_by
from .models import Flier, Photo, YoutubeVideo


class FlierAdmin(admin.ModelAdmin):
    list_display = ('show', 'priority', 'image', 'date', meta_created_date, meta_created_by)
    list_filter = ('date', 'priority',  'show')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'priority', 'caption', 'artist', 'show', 'date', meta_created_date, meta_created_by)
    list_filter = ('date', 'priority', 'artist', 'show')


class YoutubeAdmin(admin.ModelAdmin):
    list_display = ('caption', 'priority', 'youtube_url', 'artist', 'show', 'date', meta_created_date,
                    meta_created_by)
    list_filter = ('date', 'priority', 'artist', 'show')


admin.site.register(Flier, FlierAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(YoutubeVideo, YoutubeAdmin)
