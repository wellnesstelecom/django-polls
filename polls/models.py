# -*- encoding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from decimal import *


class QuestionManager(models.Manager):

    def create_poll(self, poll, question, choices):
        """ create a poll with available chices 
            choices must be an iterable object
        """
        q = Question(poll=poll, question=question)
        q.save()
        for c in choices:
            Choice(text=c, question=q).save()
        return q

class Poll(models.Model):
    """ poll """

    title = models.TextField(_('title'))
    description = models.TextField(_('Poll description'), blank=True)

    def __unicode__(self):
        return self.title

    def add_question(self, question, answers):
        Question.objects.create_poll(self, question, answers)

class Question(models.Model):
    """ poll question """

    question = models.TextField(_('question'))
    poll = models.ForeignKey(Poll, related_name="questions")

    objects = QuestionManager()

    def user_choice(self, user):
        """ return user choice for this poll """
        try:
            return UserChoice.objects.get(user=user, choice__question=self).choice
        except UserChoice.DoesNotExist:
            pass
        return None

    def votes(self):
        """ return the vote number """
        return UserChoice.objects.filter(choice__question=self).count()

    def __unicode__(self):
        return self.question


class Choice(models.Model):
    """ poll choice """

    question = models.ForeignKey(Question, related_name="choices")
    text = models.CharField(_('answer'), max_length=255)

    def __unicode__(self):
      return self.text

    def vote(self, user):
        """ user vote for this choice """
        if not self.question.user_choice(user):
            UserChoice(user=user, choice=self).save()
            return True
        return False

    def votes(self):
        return self.users.all().count()

    def percentage(self):
      total = self.question.votes()
      if total == 0:
          return 0
      return round((self.votes()*100.0)/total,1)

class UserChoice(models.Model):
    """
    it represents the vote for each user with timestamp
    """
    choice = models.ForeignKey(Choice, related_name="users")
    user = models.ForeignKey(User, related_name="polL_choices")
    timestamp = models.DateTimeField(default=datetime.now)

    class Meta:
        unique_together = ("choice", "user")

