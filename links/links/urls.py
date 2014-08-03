from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/maker/', include('maker.urls')),
    url(r'^api/v1/folder/', include('maker.urls'))
)
