# -*- encoding: utf-8 -*-
#
# author félix lópez

import datetime

from django.test import TestCase
from polls.models import Poll, Choice, UserChoice, Question
from django.contrib.auth.models import User

class PollTest(TestCase):

    def setUp(self):
        self.poll = Poll(title='test')
        self.poll.save()

    def test_add_question(self):
        self.poll.add_question('question', ['ans1', 'ans2'])
        self.assertEquals(1, self.poll.questions.all().count())

class QuestionTest(TestCase):

    def setUp(self):
        self.user = User(username="test")
        self.user.save()
        self.user2 = User(username="test2")
        self.user2.save()
        self.poll = Poll(title="test")
        self.poll.save()

    def test_create_poll(self):
        q = Question.objects.create_poll(self.poll, "question", ["answer1", "answer2"])
        self.assertEquals(2, q.choices.all().count())

    def test_user_choice(self):
        q = Question.objects.create_poll(self.poll, "question", ["answer1", "answer2"])
        choice = q.choices.all()[0]
        UserChoice(user=self.user, choice=choice).save()
        self.assertEquals(choice.id, q.user_choice(self.user).id)

    def test_vote_choice(self):
        q = Question.objects.create_poll(self.poll, "question", ["answer1", "answer2"])
        choice = q.choices.all()[0]
        choice.vote(self.user)
        self.assertEquals(1, choice.users.all().count())

    def test_vote_twice(self):
        q = Question.objects.create_poll(self.poll, "question", ["answer1", "answer2"])
        choice = q.choices.all()[0]
        choice.vote(self.user)
        choice.vote(self.user)
        self.assertEquals(1, choice.users.all().count())

    def test_percentage(self):
        q = Question.objects.create_poll(self.poll, "question", ["answer1", "answer2"])
        choice= q.choices.all()[0]
        choice.vote(self.user)
        q.choices.all()[1].vote(self.user2)
        self.assertAlmostEquals(50, choice.percentage())




