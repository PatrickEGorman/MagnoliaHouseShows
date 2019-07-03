from rest_framework import serializers

from .models import Show
from music.serializers import ArtistSerializer, GenreSerializer


class ShowSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    time = serializers.TimeField()
    suggested_donation = serializers.IntegerField()
    facebook = serializers.URLField()
    description = serializers.CharField()
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
                  'artists',
                  'genres')


