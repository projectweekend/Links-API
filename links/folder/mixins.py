from folder.models import Folder
from folder.serializers import FolderSerializer, FolderExtendedSerializer


class FolderAPI(object):

    filter_fields = ('is_public',)
    ordering_fields = ('name', 'is_public',)

    def get_queryset(self):
        return Folder.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FolderExtendedSerializer
        return FolderSerializer


class FolderSelfAPI(object):

    def get_queryset(self):
        return Folder.objects.filter(owner=self.request.user)

    def pre_save(self, obj):
           obj.owner = self.request.user
