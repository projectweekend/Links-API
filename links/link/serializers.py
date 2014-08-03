from rest_framework import serializers

from link.models import Link


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ('id', 'folder', 'url', 'note', 'photo_url', 'created')
        read_only_fields = ('photo_url', 'created')
