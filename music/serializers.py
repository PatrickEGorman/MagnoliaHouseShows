from rest_framework import serializers

from main.serializers import MetaDataSerializer
from .models import Album, Artist, Genre


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    metaData = MetaDataSerializer()

    class Meta:
        model = Genre
        fields = ('id',
                  'name',
                  'metaData')


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
    metaData = MetaDataSerializer()

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
                  'bandcamp_embed_code',
                  'metaData')


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
    metaData = MetaDataSerializer()

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
                  'bandcamp_embed_code',
                  'metaData')
