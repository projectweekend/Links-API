from django.conf.urls import patterns, include, url

from maker.views import (RegsitrationView, AuthenticationView, MakerSelfView)


urlpatterns = patterns(
    '',
    url(
        r'^/?$',
        MakerSelfView.as_view()
    ),
    url(
        r'^register/?$',
        RegsitrationView.as_view()
    ),
    url(
        r'^authenticate/?$',
        AuthenticationView.as_view()
    )
)
