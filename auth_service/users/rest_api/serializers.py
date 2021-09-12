from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "password"
        ]


class UserOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "uuid",
            "username",
            "first_name",
            "last_name",
        ]
