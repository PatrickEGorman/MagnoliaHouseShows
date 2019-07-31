from rest_framework import serializers

from main.serializers import MetaDataSerializer
from music.serializers import ArtistSerializer
from shows.models import Show
from .models import Flier, Photo, YoutubeVideo


class ShowEmbedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    date_string = serializers.CharField()
    genres = serializers.DictField()
    name = serializers.CharField()
    time = serializers.TimeField()
    metaData = MetaDataSerializer()

    class Meta:
        model = Show
        fields = ('id',
                  'date',
                  'date_string',
                  'genres',
                  "name",
                  "time",
                  'metaData')


class FlierSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()
    date = serializers.DateField()
    caption = serializers.CharField()
    year_month = serializers.ListField()
    date_string = serializers.CharField()
    show = ShowEmbedSerializer()
    metaData = MetaDataSerializer()

    class Meta:
        model = Flier
        fields = ('id',
                  'image',
                  'date',
                  'caption',
                  'year_month',
                  'date_string',
                  'show',
                  'metaData')


class PhotoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()
    date = serializers.DateField()
    caption = serializers.CharField()
    year_month = serializers.ListField()
    date_string = serializers.CharField()
    artist = ArtistSerializer()
    show = ShowEmbedSerializer()
    metaData = MetaDataSerializer()

    class Meta:
        model = Photo
        fields = ('id',
                  'image',
                  'date',
                  'caption',
                  'year_month',
                  'date_string',
                  'artist',
                  'show',
                  'metaData')


class YoutubeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    youtube_url = serializers.URLField()
    caption = serializers.CharField()
    year_month = serializers.ListField()
    date_string = serializers.CharField()
    artist = ArtistSerializer()
    show = ShowEmbedSerializer()
    metaData = MetaDataSerializer()

    class Meta:
        model = YoutubeVideo
        fields = ('id',
                  'date',
                  'youtube_url',
                  'caption',
                  'year_month',
                  'date_string',
                  'artist',
                  'show',
                  'metaData')
