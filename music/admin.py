from django.contrib import admin
from .models import Album, Band, Genre, Song


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'bandcamp')


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'hometown', 'bandcamp')


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


class SongAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Album, AlbumAdmin)
admin.site.register(Band, BandAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Song, SongAdmin)