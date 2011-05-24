# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^(?P<poll_id>\d+)/$', 'test_app.views.index', name='test'),
)
