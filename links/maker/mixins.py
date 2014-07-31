from maker.models import Maker
from maker.serializers import (MakerReadSerializer, MakerUpdateSerializer)


class AuthenticatedMaker(object):

    def get_queryset(self):
        return Maker.objects.get(pk=self.request.user.pk)

    def get_object(self):
        return self.get_queryset()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return MakerUpdateSerializer
        return MakerReadSerializer
