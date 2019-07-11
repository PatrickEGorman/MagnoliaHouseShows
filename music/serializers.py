from rest_framework import serializers

from .models import Album, Artist, Genre


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

    class Meta:
        model = Genre
        fields = ('id',
                  'name')


class ArtistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    hometown = serializers.CharField()
    genres = GenreSerializer(many=True)
    bandcamp_embed_code = serializers.CharField()
    soundcloud_embed_code = serializers.CharField()
    youtube_embed_code = serializers.CharField()
    bandcamp = serializers.URLField()
    facebook = serializers.URLField()
    soundcloud = serializers.URLField()
    youtube = serializers.URLField()
    description = serializers.CharField()

    class Meta:
        model = Artist
        fields = ('id',
                  'name',
                  'hometown',
                  'genres',
                  'bandcamp',
                  'facebook',
                  'soundcloud',
                  'youtube',
                  'description',
                  'soundcloud_embed_code',
                  'youtube_embed_code',
                  'bandcamp_embed_code')


class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    genres = GenreSerializer(many=True)
    release_date = serializers.DateField()
    bandcamp = serializers.URLField()
    youtube = serializers.URLField()
    artist = ArtistSerializer()
    cover_image = serializers.ImageField()
    description = serializers.CharField()
    bandcamp_embed_code = serializers.CharField()
    youtube_embed_code = serializers.CharField()

    class Meta:
        model = Album
        fields = ('id',
                  'name',
                  'genres',
                  'release_date',
                  'bandcamp',
                  'youtube',
                  'artist',
                  'cover_image',
                  'description',
                  'youtube_embed_code',
                  'bandcamp_embed_code')
