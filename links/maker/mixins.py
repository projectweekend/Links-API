from maker.models import Maker
from maker.serializers import MakerSerializer


class AuthenticatedMaker(object):

    serializer_class = MakerSerializer

    def get_queryset(self):
        return Maker.objects.get(pk=self.request.user.pk)

    def get_object(self):
        return self.get_queryset()
