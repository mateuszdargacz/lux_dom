# -*- coding: utf-8 -*-
__author__ = 'mateusz'
__date__ = '13.11.14 / 09:09'
__git__ = 'https://github.com/mateuszdargacz'


from django.conf.urls import patterns, include, url
from django.conf import settings

    # Examples:
urlpatterns = patterns('apps.core.views',
    url(r'^/?$', 'main', name='main'),
    url(r'^hood/?$', 'hood', name='hood'),
    url(r'^houses/(?P<pk>\d+)/?$', 'houses', name='houses'),
    url(r'^gallery/?$', 'gallery', name='gallery'),
    url(r'^contact/?$', 'contact', name='contact'),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
