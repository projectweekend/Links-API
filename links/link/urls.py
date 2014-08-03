from django.conf.urls import patterns, url

from link.views import (LinkSelfListView, LinkSelfDetailView)


urlpatterns = patterns(
    '',
    url(
        r'^/?$',
        LinkSelfListView.as_view(),
        name='link-self-list'
    ),
    url(
        r'^(?P<pk>[0-9]+)/?$',
        LinkSelfDetailView.as_view(),
        name='link-self-detail'
    )
)
