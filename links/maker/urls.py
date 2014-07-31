from django.conf.urls import patterns, include, url

from maker.views import (RegsitrationView)


urlpatterns = patterns(
    '',
    url(
        r'^register/?$',
        RegsitrationView.as_view()
    )
)
