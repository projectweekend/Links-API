from rest_framework import serializers

from maker.models import Maker
from folder.serializers import FolderExtendedSerializer
from link.serializers import LinkSerializer


class RegistrationRequestSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)


class EmailVerificationProcessSerializer(serializers.Serializer):

    token = serializers.CharField(required=True)


class AuthenticationResponseSerializer(serializers.Serializer):

    token = serializers.CharField()


class AuthenticationRequestSerializer(serializers.Serializer):

    identifier = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class ResetPasswordRequestSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)


class ResetPasswordProcessSerializer(serializers.Serializer):

    token = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError("'new_password' and 'confirm_password' do not match")
        return attrs


class ChangePasswordSerializer(serializers.Serializer):

    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError("'new_password' and 'confirm_password' do not match")
        return attrs


class EmailChangeRequestSerializer(serializers.Serializer):

    new_email = serializers.EmailField(required=True)


class EmailChangeProcessSerializer(serializers.Serializer):

    token = serializers.CharField(required=True)


class MakerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Maker
        fields = ('id', 'identifier', 'first_name', 'last_name', 'email',
                    'photo_url', 'bio', 'joined')
        read_only_fields = ('identifier', 'email', 'joined',)


class MakerProfileSerializer(serializers.ModelSerializer):

    folders = serializers.SerializerMethodField('public_folders')
    links = serializers.SerializerMethodField('uncategorized_links')

    class Meta:
        model = Maker
        fields = ('id', 'identifier', 'first_name', 'last_name', 'email',
                    'photo_url', 'folders', 'links', 'bio', 'joined')

    def public_folders(self, obj):
        query_set = obj.folders.filter(is_public=True)
        serializer = FolderExtendedSerializer(instance=query_set, many=True)
        return serializer.data

    def uncategorized_links(self, obj):
        query_set = obj.links.filter(folder=None)
        serializer = LinkSerializer(instance=query_set, many=True)
        return serializer.data
