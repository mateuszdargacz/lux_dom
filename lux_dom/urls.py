from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('apps.core.urls', namespace="core")),
    url(r'^zohoverify/verifyforzoho.html/?$', TemplateView.as_view(template_name='zoho.html'), name='gallery'),
    url(r'^admin/', include(admin.site.urls)),
)

# Uncomment the next line to serve media files in dev.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

