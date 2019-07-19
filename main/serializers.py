from rest_framework import serializers

from accounts.serializers import UserSerializer
from main.models import MetaData


class MetaDataSerializer(serializers.ModelSerializer):
    post_name = serializers.CharField()

    posted_on = serializers.DateField()
    posted_by = UserSerializer()
    last_updated_on = serializers.DateField()
    last_updated_by = UserSerializer()

    posted_date_string = serializers.CharField()
    posted_string = serializers.CharField()
    updated_date_string = serializers.CharField()
    updated_string = serializers.CharField()

    class Meta:
        model = MetaData
        fields = (
                'post_name',
                'posted_on',
                'posted_by',
                'last_updated_on',
                'last_updated_by',
                'posted_string',
                'posted_date_string',
                'updated_string',
                'updated_date_string'
            )
