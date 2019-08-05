from rest_framework import serializers

from main.serializers import MetaDataSerializer
from shows.models import Show
from .models import Album, Artist, Genre


class EmbedGenreSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Genre
        fields = ('id',
                  'name')


class EmbedArtistSerializer(serializers.ModelSerializer):
    genres = EmbedGenreSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('id',
                  'genres',
                  'bandcamp_embed_code',
                  'name')


class ShowEmbedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    date_string = serializers.CharField()
    name = serializers.CharField()
    time = serializers.TimeField()
    suggested_donation = serializers.IntegerField()
    suggested_donation_max = serializers.IntegerField()
    artists = EmbedArtistSerializer(many=True)
    metaData = MetaDataSerializer()

    class Meta:
        model = Show
        fields = ('id',
                  'date',
                  'date_string',
                  'genres',
                  "name",
                  "time",
                  "artists",
                  "suggested_donation",
                  "suggested_donation_max",
                  'metaData')


class ArtistEmbedGenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    show_set = ShowEmbedSerializer(many=True)
    genres = EmbedGenreSerializer(many=True)
    hometown = serializers.CharField()
    bandcamp_embed_code = serializers.CharField()
    soundcloud_embed_code = serializers.CharField()
    youtube_embed_code = serializers.CharField()
    bandcamp = serializers.URLField()
    facebook = serializers.URLField()
    soundcloud = serializers.URLField()
    youtube = serializers.URLField()
    metaData = MetaDataSerializer()

    class Meta:
        model = Artist
        fields = ('id',
                  'name',
                  'show_set',
                  'genres',
                  "hometown",
                  "description",
                  'bandcamp_embed_code',
                  'soundcloud_embed_code',
                  "youtube_embed_code",
                  "bandcamp",
                  "facebook",
                  "soundcloud",
                  "youtube",
                  'metaData')


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    metaData = MetaDataSerializer()
    artist_set = ArtistEmbedGenreSerializer(many=True)
    description = serializers.CharField()

    class Meta:
        model = Genre
        fields = ('id',
                  'name',
                  'artist_set',
                  'description',
                  'metaData')


class GenreListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    artist_set = EmbedArtistSerializer(many=True)
    description = serializers.CharField()

    class Meta:
        model = Genre
        fields = ('id',
                  'name',
                  'artist_set',
                  'description')


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
    show_set = ShowEmbedSerializer(many=True)
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
                  'show_set',
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
