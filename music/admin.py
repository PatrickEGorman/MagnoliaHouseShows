from django.contrib import admin

from main.admin import meta_created_date, meta_created_by
from .models import Album, Artist, Genre


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'priority', 'bandcamp', 'release_date', 'display_genre', meta_created_date,
                    meta_created_by)
    list_filter = ['artist', 'priority', 'release_date', 'genres']
    fields = [('name', 'artists'), 'priority', ('bandcamp_embed_code', 'youtube_embed_code'), 'description',
              ('suggested_donation', 'suggested_donation_max'), ('facebook', 'instagram')]


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'priority', 'hometown', 'display_genre', meta_created_date, meta_created_by)
    list_filter = ['hometown', 'priority', 'genres']
    fields = ['name', 'priority', 'hometown', 'genres', ('bandcamp_embed_code', 'soundcloud_embed_code', 'youtube_embed_code'),
              ('bandcamp', 'soundcloud', 'youtube', 'facebook'), 'description']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'priority']


admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre, GenreAdmin)
