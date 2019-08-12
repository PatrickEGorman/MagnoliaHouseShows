from rest_framework import serializers

from main.serializers import MetaDataSerializer
from media.serializers import FlierSerializer, PhotoSerializer, YoutubeSerializer
from music.models import Artist, Genre

from .models import Show
from music.serializers import ArtistSerializer, EmbedGenreSerializer


class ShowSerializer(serializers.ModelSerializer):
    flier = FlierSerializer()
    artists = ArtistSerializer(many=True)
    photos = PhotoSerializer(many=True)
    videos = YoutubeSerializer(many=True)
    metaData = MetaDataSerializer()

    class Meta:
        model = Show
        fields = ('id',
                  'date',
                  'time',
                  'suggested_donation',
                  'suggested_donation_max',
                  'description',
                  'facebook',
                  'instagram',
                  'year_month',
                  'date_string',
                  'artists',
                  'photos',
                  'videos',
                  'genres',
                  'sorted_genres',
                  'flier',
                  "name",
                  'metaData',
                  'cancelled')


class ArtistEmbedListShowSerializer(serializers.ModelSerializer):
    genres = EmbedGenreSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('id',
                  'name',
                  'hometown',
                  'genres')


class ListShowSerializer(serializers.ModelSerializer):

    artists = ArtistEmbedListShowSerializer(many=True)

    class Meta:
        model = Show
        fields = ('id',
                  'date',
                  'time',
                  'suggested_donation',
                  'suggested_donation_max',
                  'description',
                  'facebook',
                  'instagram',
                  'year_month',
                  'date_string',
                  'artists',
                  'genres',
                  'sorted_genres',
                  "name",
                  'cancelled')
