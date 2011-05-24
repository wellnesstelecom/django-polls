#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# Félix López Luís

import logging


from django import template
from django.contrib.auth.models import User, AnonymousUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from polls.models import Poll, UserChoice


register = template.Library()


@register.filter
def get_user_vote(value, arg):
    try:
        poll = value
        user = arg
        if not user.is_anonymous():
            return poll.get_user_choice(user)
        else:
            return False

    except ObjectDoesNotExist:
        logging.error("La consulta no existe")
        return False


@register.filter
def choice_for(user, question):
    """ return user choice for this question """
    return question.user_choice(user)



register.filter('get_user_vote', get_user_vote)


@register.inclusion_tag('polls/poll_results.html')
def poll_results(poll):
    return {'poll': poll}

@register.inclusion_tag('polls/poll_detail.html', takes_context=True)
def poll_show(context, poll, next=None):
    next = next or context['request'].path
    return {'poll': poll, 
            'user': context['user'],
            'next': next }

#@register.simple_tag





