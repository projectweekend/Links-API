from link.models import Link
from link.serializers import LinkSerializer


class LinkAPI(object):

    serializer_class = LinkSerializer
    ordering_fields = ('title', 'created')

    def get_queryset(self):
        return Link.objects.all()


class LinkSelfAPI(object):

    def get_queryset(self):
        return Link.objects.filter(owner=self.request.user)

    def pre_save(self, obj):
        obj.owner = self.request.user
