# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Question

# Create your views here.
# all Django wants is an HttpResponse or a Http404
# this is different from what DjangoGirls did with render

def index(request):
    # get the 5 latest updates
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    output = ', '.join([q.question_text for q in latest_question_list])

    return HttpResponse(output)
    # return HttpResponse("Hello, world. You're at the polls index.")


def details(request, question_id):
    return HttpResponse("You are looking at question %s." % question_id)

def results(request, question_id):
    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('You are voting on question %s.' % question_id)