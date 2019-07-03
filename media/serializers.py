from rest_framework import serializers

from shows.serializers import ShowSerializer
from music.serializers import ArtistSerializer
from .models import Flier, Photo, YoutubeVideo


class FlierSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()
    date = serializers.DateField()
    caption = serializers.CharField()
    show = ShowSerializer()

    class Meta:
        model = Flier
        fields = ('id',
                  'image',
                  'date',
                  'caption',
                  'show')


class PhotoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()
    date = serializers.DateField()
    caption = serializers.CharField()
    artist = ArtistSerializer()
    show = ShowSerializer()

    class Meta:
        model = Photo
        fields = ('id',
                  'image',
                  'date',
                  'caption',
                  'artist',
                  'show')


class YoutubeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    youtube_url = serializers.URLField()
    caption = serializers.CharField()
    artist = ArtistSerializer()
    show = ShowSerializer()

    class Meta:
        model = YoutubeVideo
        fields = ('id',
                  'date',
                  'youtube_url',
                  'caption',
                  'artist',
                  'show')
