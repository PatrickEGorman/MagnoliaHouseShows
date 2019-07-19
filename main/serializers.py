from rest_framework import serializers

from accounts.serializers import UserSerializer
from main.models import MetaData


class MetaDataSerializer(serializers.ModelSerializer):
    post_name = serializers.CharField()

    posted_on = serializers.DateField()
    posted_by = UserSerializer()
    last_updated_on = serializers.DateField()
    last_updated_by = UserSerializer()

    posted_date = serializers.CharField()
    posted_string = serializers.CharField()
    last_updated_date = serializers.CharField()
    last_updated_string = serializers.CharField()

    class Meta:
        model = MetaData
        fields = (
                'post_name',
                'posted_on',
                'posted_by',
                'last_updated_on',
                'last_updated_by',
                'posted_date',
                'posted_string',
                'last_updated_date',
                'last_updated_string'
            )
