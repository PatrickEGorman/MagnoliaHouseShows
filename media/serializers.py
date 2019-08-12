from rest_framework import serializers

from main.serializers import MetaDataSerializer
from music.serializers import ArtistSerializer
from shows.models import Show
from .models import Flier, Photo, YoutubeVideo


class ShowEmbedMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Show
        fields = ('id',
                  'date',
                  'date_string',
                  'genres',
                  "name",
                  "time")


class FlierSerializer(serializers.ModelSerializer):

    show = ShowEmbedMediaSerializer()
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

    artist = ArtistSerializer()
    show = ShowEmbedMediaSerializer()
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

    artist = ArtistSerializer()
    show = ShowEmbedMediaSerializer()
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
