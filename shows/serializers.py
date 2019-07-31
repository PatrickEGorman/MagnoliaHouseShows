from rest_framework import serializers

from main.serializers import MetaDataSerializer
from media.serializers import FlierSerializer

from .models import Show
from music.serializers import ArtistSerializer, GenreSerializer, ArtistEmbedGenreSerializer


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
                  'metaData')


class ShowMinSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    time = serializers.TimeField()
    suggested_donation = serializers.IntegerField()
    suggested_donation_max = serializers.IntegerField()
    description = serializers.CharField()
    year_month = serializers.ListField()
    date_string = serializers.CharField()
    artists = ArtistEmbedGenreSerializer(many=True)
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
                  'year_month',
                  'date_string',
                  'artists',
                  'genres',
                  'sorted_genres',
                  "name",
                  'metaData')


