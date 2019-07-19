from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = CustomUser
        fields = (
            'name',
            'username',
            'first_name',
            'last_name',
            'email'
        )
