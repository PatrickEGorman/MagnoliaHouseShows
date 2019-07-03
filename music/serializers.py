from rest_framework import serializers

from .models import Album, Artist, Genre, Song


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
    bandcamp = serializers.URLField()
    facebook = serializers.URLField()
    soundcloud = serializers.URLField()
    youtube = serializers.URLField()

    class Meta:
        model = Artist
        fields = ('id',
                  'name',
                  'hometown',
                  'genres',
                  'bandcamp',
                  'facebook',
                  'soundcloud',
                  'youtube')


class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    genres = GenreSerializer(many=True)
    release_date = serializers.DateField()
    bandcamp = serializers.URLField()
    youtube = serializers.URLField()
    artist = ArtistSerializer()
    cover_image = serializers.ImageField()

    class Meta:
        model = Album
        fields = ('id',
                  'name',
                  'genres',
                  'release_date',
                  'bandcamp',
                  'youtube',
                  'artist',
                  'cover_image')


class SongSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    genres = GenreSerializer(many=True)
    album = AlbumSerializer()

    class Meta:
        model = Song
        fields = ('id',
                  'name',
                  'genres',
                  'album')
