from django.contrib import admin
from .models import Flier, Photo, YoutubeVideo


class FlierAdmin(admin.ModelAdmin):
    list_display = ('show', 'image')


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image', 'caption', 'band', 'show')


class YoutubeAdmin(admin.ModelAdmin):
    list_display = ('caption', 'youtube_url', 'show')


admin.site.register(Flier, FlierAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(YoutubeVideo, YoutubeAdmin)
