from main.serializers import MetaDataSerializer
from music.serializers import ArtistSerializer
from shows.serializers import ShowSerializer
from .models import History

from rest_framework import serializers


class HistorySerializer(serializers.ModelSerializer):

    artists = ArtistSerializer(many=True)
    shows = ShowSerializer(many=True)
    metaData = MetaDataSerializer()

    class Meta:
        model = History
        fields = {
            'image',
            'image_caption',
            'title',
            'text',
            'artists',
            'shows',
            'start_or_primary_date',
            'end_date',
            'metaData'
        }