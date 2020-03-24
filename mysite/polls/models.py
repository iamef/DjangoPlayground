# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models

# Create your models here.
# each model has class variables
# each variable represents a database field
from django.utils import timezone


class Question(models.Model):
    # question_text and pub_date are field names
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return timezone.now() - self.pub_date <= datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # ForeignKey tells Django that each choice is related to a single question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
