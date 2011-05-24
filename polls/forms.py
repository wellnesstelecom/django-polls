#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: maria amor

from django import forms
from django.forms import widgets


class QuestionForm(forms.Form):

    answer = forms.ChoiceField(widget=widgets.RadioSelect)

    def __init__(self, answers ):
        self.fields['choices'].choices = enumerate(answers)

    def save(self):
        pass

