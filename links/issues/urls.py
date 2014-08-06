from django.conf.urls import patterns, url

from issues.views import (ReportedLinkCreateView, ReportedUserCreateView)


urlpatterns = patterns(
    '',
    url(
        r'^report/link/?$',
        ReportedLinkCreateView.as_view(),
        name='report-link-view'
    ),
    url(
        r'^report/user/?$',
        ReportedUserCreateView.as_view(),
        name='report-user-view'
    )
)
