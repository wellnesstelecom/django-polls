#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: javi santana

from django.db import models

class PollManager(models.Manager):

    def create_poll(self, question, choices):
        """ create a poll with available chices 
            choices must be an iterable object
        """
        poll = Poll(question=question)
        poll.save()
        for c in choices:
            Choice(text=c, poll=poll).save()
        return poll
