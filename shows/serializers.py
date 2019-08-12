from rest_framework import serializers

from main.serializers import MetaDataSerializer
from media.serializers import FlierSerializer
from music.models import Artist, Genre

from .models import Show
from music.serializers import ArtistSerializer


class ShowSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    time = serializers.TimeField()
    suggested_donation = serializers.IntegerField()
    suggested_donation_max = serializers.IntegerField()
    facebook = serializers.URLField()
    instagram = serializers.URLField()
    description = serializers.CharField()
    year_month = serializers.ListField()
    date_string = serializers.CharField()
    fliers = FlierSerializer(many=True)
    artists = ArtistSerializer(many=True)
    genres = serializers.DictField()
    sorted_genres = serializers.ListField()
    name = serializers.CharField()
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
                  'genres',
                  'sorted_genres',
                  'fliers',
                  "name",
                  'metaData',
                  'cancelled')


class GenreEmbedListShowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('id',
                  'name')


class ArtistEmbedListShowSerializer(serializers.ModelSerializer):
    genres = GenreEmbedListShowSerializer(many=True)

    class Meta:
        model = Artist
        fields = ('id',
                  'name',
                  'hometown',
                  'genres')


class ListShowSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    time = serializers.TimeField()
    suggested_donation = serializers.IntegerField()
    suggested_donation_max = serializers.IntegerField()
    facebook = serializers.URLField()
    instagram = serializers.URLField()
    year_month = serializers.ListField()
    date_string = serializers.CharField()
    artists = ArtistEmbedListShowSerializer(many=True)
    genres = serializers.DictField()
    sorted_genres = serializers.ListField()
    name = serializers.CharField()

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
                  'fliers',
                  "name",
                  'cancelled')
