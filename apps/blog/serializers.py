from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class MySerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']