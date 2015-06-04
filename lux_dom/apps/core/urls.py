# -*- coding: utf-8 -*-
__author__ = 'mateusz'
__date__ = '13.11.14 / 09:09'
__git__ = 'https://github.com/mateuszdargacz'


from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = patterns('apps.core.views',
    # Examples:
    url(r'^main/?$', TemplateView.as_view(template_name="core/main.html"), name='main'),
    # url(r'^{{ project_name }}/', include('{{ project_name }}.foo.urls')),
)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
