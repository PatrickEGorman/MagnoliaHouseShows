from rest_framework import serializers

from main.serializers import MetaDataSerializer
from media.models import Photo, YoutubeVideo, Flier
from shows.models import Show
from .models import Album, Artist, Genre


class EmbedGenreSerializer(serializers.ModelSerializer):

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
                  'name')


class FlierEmbedMusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flier
        fields = ('id',
                  'image',
                  'caption')


class ShowEmbedMusicSerializer(serializers.ModelSerializer):

    artists = EmbedArtistSerializer(many=True)
    flier = FlierEmbedMusicSerializer()

    class Meta:
        model = Show
        fields = ('id',
                  'date',
                  'date_string',
                  "name",
                  "time",
                  "artists",
                  "suggested_donation",
                  "suggested_donation_max",
                  'flier')


class ArtistEmbedGenreSerializer(serializers.ModelSerializer):

    show_set = ShowEmbedMusicSerializer(many=True)

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


class PhotoEmbedArtistSerializer(serializers.ModelSerializer):

    show = ShowEmbedMusicSerializer()

    class Meta:
        model = Photo
        fields = ('id',
                  'image',
                  'caption',
                  'date',
                  'show')


class VideoEmbedArtistSerializer(serializers.ModelSerializer):

    show = ShowEmbedMusicSerializer()

    class Meta:
        model = YoutubeVideo
        fields = ('id',
                  'youtube_url',
                  'caption',
                  'date',
                  'show')


class ArtistSerializer(serializers.ModelSerializer):

    photos = PhotoEmbedArtistSerializer(many=True)
    videos = VideoEmbedArtistSerializer(many=True)
    genres = EmbedGenreSerializer(many=True)
    show_set = ShowEmbedMusicSerializer(many=True)
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
                  'metaData',
                  'photos',
                  'videos')


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
