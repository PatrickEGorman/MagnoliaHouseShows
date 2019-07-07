from django.contrib import admin
from .models import Album, Artist, Genre


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'bandcamp', 'release_date')


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'hometown', 'bandcamp')


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre, GenreAdmin)
