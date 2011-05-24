# -*- encoding: utf-8 -*-

from polls.models import Poll
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


@login_required
def index(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('index.html', {'poll': poll},
            context_instance=RequestContext(request))

