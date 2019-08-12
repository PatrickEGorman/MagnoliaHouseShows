from rest_framework import serializers

from main.serializers import MetaDataSerializer
from shows.models import Show
from .models import Album, Artist, Genre


class EmbedArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('id',
                  'genres',
                  'name')


class ShowEmbedSerializer(serializers.ModelSerializer):

    artists = EmbedArtistSerializer(many=True)

    class Meta:
        model = Show
        fields = ('id',
                  'date',
                  'date_string',
                  "name",
                  "time",
                  "artists",
                  "suggested_donation",
                  "suggested_donation_max")


class ArtistEmbedGenreSerializer(serializers.ModelSerializer):

    show_set = ShowEmbedSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('id',
                  'name',
                  'show_set',
                  "hometown",
                  "description",
                  'bandcamp_embed_code',
                  'soundcloud_embed_code',
                  "youtube_embed_code",
                  "bandcamp",
                  "facebook",
                  "soundcloud",
                  "youtube")


class GenreSerializer(serializers.ModelSerializer):

    artist_set = ArtistEmbedGenreSerializer(many=True)
    metaData = MetaDataSerializer()

    class Meta:
        model = Genre
        fields = ('id',
                  'name',
                  'artist_set',
                  'description',
                  'metaData')


class GenreListSerializer(serializers.ModelSerializer):

    artist_set = ArtistEmbedGenreSerializer(many=True)

    class Meta:
        model = Genre
        fields = ('id',
                  'name',
                  'artist_set',
                  'description')


class ArtistSerializer(serializers.ModelSerializer):

    genres = GenreSerializer(many=True)
    show_set = ShowEmbedSerializer(many=True)
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

    genres = GenreSerializer(many=True)
    artist = ArtistSerializer()
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
