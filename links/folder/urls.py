from django.conf.urls import patterns, url

from folder.views import (FolderSelfListView,
                            FolderSelfDetailView)


urlpatterns = patterns(
    '',
    url(
        r'^/?$',
        FolderSelfListView.as_view(),
        name='folder-self-list'
    ),
    url(
        r'^/(?P<pk>[0-9]+)/?$',
        FolderSelfDetailView.as_view(),
        name='folder-self-detail'
    )
)
