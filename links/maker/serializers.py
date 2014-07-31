from rest_framework import serializers


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
