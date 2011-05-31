#!/usr/bin/python
# -*- encoding: utf-8 -*-

import logging
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect,\
                        HttpResponseForbidden, HttpResponseBadRequest,\
                        HttpResponseServerError
from models import Poll,Choice
from django.utils import simplejson
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.translation import ugettext as _


@login_required(redirect_field_name=REDIRECT_FIELD_NAME)
def poll_vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    for c in request.POST.keys():
        if "choice_" in c:
            try: 
                choice = Choice.objects.get(pk=request.POST[c])
                # security check
                if choice.question.poll.id == p.id:
                    choice.vote(request.user)
            except Choice.DoesNotExist:
                pass
    url_detail = reverse('poll_detail', args=(p.id,))
    next = request.GET.get('next', url_detail)
    return HttpResponseRedirect(next)

@login_required(redirect_field_name=REDIRECT_FIELD_NAME)
def poll_detail(request, poll_id, template='polls/poll_detail.html'):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/poll_detail.html', {
                'poll': poll,
            },
            context_instance=RequestContext(request))

@login_required(redirect_field_name=REDIRECT_FIELD_NAME)
def poll_results(request, poll_id, template='polls/poll_results.html'):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/poll_results.html', {
                'poll': poll,
            },
            context_instance=RequestContext(request))
