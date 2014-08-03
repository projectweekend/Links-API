from django.conf.urls import patterns, url

from maker.views import (RegsitrationView,
                            AuthenticationView,
                            MakerSelfView,
                            MakerProfileView,
                            ResetPasswordRequestView,
                            ResetPasswordProcessView,
                            ChangePasswordView,
                            EmailChangeRequestView,
                            EmailChangeProcessView)


urlpatterns = patterns(
    '',
    url(
        r'^self/?$',
        MakerSelfView.as_view(),
        name='maker-self'
    ),
    url(
        r'^register/?$',
        RegsitrationView.as_view(),
        name='registration'
    ),
    url(
        r'^authenticate/?$',
        AuthenticationView.as_view(),
        name='authentication'
    ),
    url(
        r'^password/?$',
        ChangePasswordView.as_view(),
        name='change-password'
    ),
    url(
        r'^password/reset/?$',
        ResetPasswordRequestView.as_view(),
        name='password-reset'
    ),
    url(
        r'^password/reset/update?$',
        ResetPasswordProcessView.as_view(),
        name='password-reset-process'
    ),
    url(
        r'^email/?$',
        EmailChangeRequestView.as_view(),
        name='email-change-request'
    ),
    url(
        r'^email/update?$',
        EmailChangeProcessView.as_view(),
        name='email-change-process'
    ),
    url(
        r'^(?P<pk>[0-9]+)/?$',
        MakerProfileView.as_view(),
        name='maker-profile-view'
    )
)
