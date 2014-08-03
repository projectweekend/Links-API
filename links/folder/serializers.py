from rest_framework import serializers

from folder.models import Folder


class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = ('id', 'name', 'description', 'is_public', 'created',)
        read_only_fields = ('created',)
