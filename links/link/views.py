from rest_framework import generics

from link.mixins import LinkAPI, LinkSelfAPI


class LinkSelfListView(LinkAPI,
                        LinkSelfAPI,
                        generics.ListCreateAPIView):
    pass


class LinkSelfDetailView(LinkAPI,
                            LinkSelfAPI,
                            generics.RetrieveUpdateDestroyAPIView):
    pass
