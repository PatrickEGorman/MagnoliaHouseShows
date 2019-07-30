from django.contrib import admin

from main.admin import meta_created_date, meta_created_by, ModelAdminWithMeta
from .models import Album, Artist, Genre


class AlbumAdmin(ModelAdminWithMeta):
    list_display = ('name', 'artist', 'priority', 'bandcamp', 'release_date', 'display_genre', meta_created_date,
                    meta_created_by)
    list_filter = ['artist', 'priority', 'release_date', 'genres']
    fields = [('name', 'artists'), 'priority', ('bandcamp_embed_code', 'youtube_embed_code'), 'description',
              ('suggested_donation', 'suggested_donation_max'), ('facebook', 'instagram')]
    ordering = ['name']


class ArtistAdmin(ModelAdminWithMeta):
    list_display = ('name', 'priority', 'hometown', 'display_genre', meta_created_date, meta_created_by)
    list_filter = ['hometown', 'priority', 'genres']
    ordering = ['name']
    fields = ['name', 'priority', 'hometown', 'genres', ('bandcamp_embed_code', 'soundcloud_embed_code', 'youtube_embed_code'),
              ('bandcamp', 'soundcloud', 'youtube', 'facebook'), 'description']


class GenreAdmin(ModelAdminWithMeta):
    list_display = ['name', 'priority']
    fields = ['name', 'priority']
    ordering = ['name']

    def save_model(self, request, obj, form, change):
        obj.metaData.last_updated_by = request.user
        if not obj.metaData.posted_by:
            obj.metaData.posted_by = request.user
        obj.metaData.save()
        super().save_model(request, obj, form, change)


admin.site.register(Album, AlbumAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre, GenreAdmin)
