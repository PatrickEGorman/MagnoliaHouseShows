from rest_framework import serializers
from media.serializers import FlierSerializer

from .models import Show
from music.serializers import ArtistSerializer, GenreSerializer


class ShowSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    time = serializers.TimeField()
    suggested_donation = serializers.IntegerField()
    facebook = serializers.URLField()
    instagram = serializers.URLField()
    description = serializers.CharField()
    fliers = FlierSerializer(many=True)
    artists = ArtistSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Show
        fields = ('id',
                  'date',
                  'time',
                  'suggested_donation',
                  'description',
                  'facebook',
                  'instagram',
                  'artists',
                  'genres',
                  'fliers')


