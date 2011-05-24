#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: maría amor

from django.conf.urls.defaults import *
from django.views.generic.list_detail import object_list


urlpatterns = patterns('',
    url(r'^poll/(?P<poll_id>\d+)/$', 'polls.views.poll_detail', name='poll_detail'),
    url(r'^poll/(?P<poll_id>\d+)/vote/$', 'polls.views.poll_vote', name='poll_vote'),
    url(r'^poll/(?P<poll_id>\d+)/results/$', 'polls.views.poll_results', name='poll_results'),
)
