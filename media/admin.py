from django.contrib import admin
from .models import Flier, Photo, YoutubeVideo


class FlierAdmin(admin.ModelAdmin):
    list_display = ('show', 'image', 'date')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'caption', 'artist', 'show', 'date')


class YoutubeAdmin(admin.ModelAdmin):
    list_display = ('caption', 'youtube_url', 'artist', 'show', 'date')


admin.site.register(Flier, FlierAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(YoutubeVideo, YoutubeAdmin)
