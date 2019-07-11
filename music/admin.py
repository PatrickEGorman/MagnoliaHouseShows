from django.contrib import admin
from .models import Album, Artist, Genre


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'bandcamp', 'release_date', 'display_genre')
    list_filter = ['artist', 'release_date', 'genres']
    fields = [('name', 'article'), 'artists', ('bandcamp_embed_code', 'youtube_embed_code'), 'description',
              ('suggested_donation', 'suggested_donation_max'), ('facebook', 'instagram')]


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'hometown', 'display_genre', 'bandcamp')
    list_filter = ['hometown', 'genres']
    fields = ['name', 'hometown', 'genres', ('bandcamp_embed_code', 'soundcloud_embed_code', 'youtube_embed_code'),
              ('bandcamp', 'soundcloud', 'youtube', 'facebook'), 'description']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre, GenreAdmin)
