from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^v1/maker/', include('maker.urls')),
    url(r'^v1/folder/', include('folder.urls')),
    url(r'^v1/link/', include('link.urls')),
    url(r'^v1/issue/', include('issues.urls')),
)
