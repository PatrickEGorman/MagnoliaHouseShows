from rest_framework import serializers

from main.serializers import MetaDataSerializer
from music.serializers import ArtistSerializer
from .models import Flier, Photo, YoutubeVideo


class FlierSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()
    date = serializers.DateField()
    caption = serializers.CharField()
    show = serializers.StringRelatedField(many=False)
    metaData = MetaDataSerializer()

    class Meta:
        model = Flier
        fields = ('id',
                  'image',
                  'date',
                  'caption',
                  'show',
                  'metaData')


class PhotoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()
    date = serializers.DateField()
    caption = serializers.CharField()
    artist = ArtistSerializer()
    show = serializers.StringRelatedField(many=False)
    metaData = MetaDataSerializer()

    class Meta:
        model = Photo
        fields = ('id',
                  'image',
                  'date',
                  'caption',
                  'artist',
                  'show',
                  'metaData')


class YoutubeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    date = serializers.DateField()
    youtube_url = serializers.URLField()
    caption = serializers.CharField()
    artist = ArtistSerializer()
    show = serializers.StringRelatedField(many=False)
    metaData = MetaDataSerializer()

    class Meta:
        model = YoutubeVideo
        fields = ('id',
                  'date',
                  'youtube_url',
                  'caption',
                  'artist',
                  'show',
                  'metaData')
