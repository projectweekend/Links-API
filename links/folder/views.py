from rest_framework import generics

from folder.mixins import FolderAPI, FolderSelfAPI


class FolderSelfListView(FolderAPI, FolderSelfAPI,
                            generics.ListCreateAPIView):
    pass


class FolderSelfDetailView(FolderAPI, FolderSelfAPI,
                            generics.RetrieveUpdateDestroyAPIView):
    pass
