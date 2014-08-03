from folder.models import Folder
from folder.serializers import FolderSerializer


class FolderAPI(object):

    serializer_class = FolderSerializer

    def get_queryset(self):
        return Folder.objects.all()


class FolderSelfAPI(object):

    serializer_class = FolderSerializer

    def get_queryset(self):
        return Folder.objects.filter(owner=self.request.user)
