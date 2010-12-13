from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
from tekpress.core.views import server_error

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/filebrowser/', include('filebrowser.urls')),
    (r'^admin/', include(admin.site.urls)),
)

handler500 = server_error

if settings.DEBUG:
    from django.views.static import serve
    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('',
                                (r'^%s(?P<path>.*)$' % _media_url,
                                serve,
                                {'document_root': settings.MEDIA_ROOT}))
    del(_media_url, serve)
    urlpatterns += patterns('',
        (r'^500/$', server_error),
    )

urlpatterns += patterns('', 
    (r'', include('tekblog.urls')),
)
