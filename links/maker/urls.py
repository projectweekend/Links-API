from django.conf.urls import patterns, url

from maker.views import (RegsitrationView,
                            AuthenticationView,
                            MakerSelfView,
                            ChangePasswordView)


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
    ),
    url(
        r'^password/?$',
        ChangePasswordView.as_view()
    )
)
