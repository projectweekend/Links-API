from folder.models import Folder
from folder.serializers import FolderSerializer


class FolderAPI(object):

    serializer_class = FolderSerializer
    filter_fields = ('is_public',)
    ordering_fields = ('name', 'is_public',)

    def get_queryset(self):
        return Folder.objects.all()


class FolderSelfAPI(object):

    def get_queryset(self):
        return Folder.objects.filter(owner=self.request.user)

    def pre_save(self, obj):
           obj.owner = self.request.user
