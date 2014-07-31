from rest_framework import serializers

from maker.models import Maker


class RegistrationRequestSerializer(serializers.Serializer):

    identifier = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)


class AuthenticationResponseSerializer(serializers.Serializer):

    token = serializers.CharField()


class AuthenticationRequestSerializer(serializers.Serializer):

    identifier = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class MakerUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Maker
        fields = ('first_name', 'last_name', 'email', 'photo_url', 'bio')


class MakerReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Maker
        fields = ('identifier', 'first_name', 'last_name', 'email',
                    'photo_url' 'bio')
