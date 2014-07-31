from maker.models import Maker
from maker.serializers import MakerReadSerializer


class AuthenticatedMaker(object):

    serializer_class = MakerReadSerializer

    def get_queryset(self):
        return Maker.objects.get(pk=self.request.user.pk)

    def get_object(self):
        return self.get_queryset()
