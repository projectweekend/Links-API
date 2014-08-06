from rest_framework import serializers

from issues.models import ReportedLink, ReportedUser


class ReportedLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportedLink
        fields = ('id', 'link', 'created')
        read_only_fields = ('created',)


class ReportedUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReportedUser
        fields = ('id', 'user', 'created')
        read_only_fields = ('created',)
