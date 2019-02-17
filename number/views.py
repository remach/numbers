from django.shortcuts import render
from number.models import Number
from django.contrib.auth.models import User, Group

from django.http import HttpResponse


# Create your views here.

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Number.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.description_text for q in latest_question_list])
    return HttpResponse(output)

