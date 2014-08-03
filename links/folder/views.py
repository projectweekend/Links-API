from django.db import IntegrityError

from rest_framework import generics, status
from rest_framework.response import Response

from folder.mixins import FolderAPI, FolderSelfAPI


class FolderSelfListView(FolderAPI, FolderSelfAPI,
                            generics.ListCreateAPIView):

    def post(self, request):
        try:
            return self.create(request)
        except IntegrityError:
            return Response(status=status.HTTP_409_CONFLICT)


class FolderSelfDetailView(FolderAPI, FolderSelfAPI,
                            generics.RetrieveUpdateDestroyAPIView):
    pass
