# -*- encoding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin

from django.views.generic.simple import direct_to_template


admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^polls/', include('polls.urls')),
    (r'', include('test_app.urls')),


)

if settings.DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                {'document_root': settings.MEDIA_ROOT}),
    )
