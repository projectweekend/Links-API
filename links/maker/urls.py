from django.conf.urls import patterns, include, url

from maker.views import (RegsitrationView, AuthenticationView)


urlpatterns = patterns(
    '',
    url(
        r'^register/?$',
        RegsitrationView.as_view()
    ),
    url(
        r'^authenticate/?$',
        AuthenticationView.as_view()
    )
)
