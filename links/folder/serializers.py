from rest_framework import serializers

from folder.models import Folder
from link.serializers import LinkSerializer


class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = ('id', 'name', 'description', 'is_public', 'created',)
        read_only_fields = ('created',)


class FolderExtendedSerializer(serializers.ModelSerializer):

    links = LinkSerializer(many=True)

    class Meta:
        model = Folder
        fields = ('id', 'name', 'description', 'links', 'is_public', 'created',)
        read_only_fields = ('created',)
