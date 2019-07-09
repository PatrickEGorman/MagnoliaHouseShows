from django.contrib import admin
from .models import Album, Artist, Genre


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'bandcamp', 'release_date', 'display_genre')


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'hometown', 'bandcamp', 'display_genre')


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre, GenreAdmin)
