from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Question

# old stuff
# def index(request):
#     return HttpResponse("Hi there, this is my first <b>view</b>")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = '<br /> '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

def detail(request, question_id):
    return HttpResponse('Question %s' % question_id)

    
def results(request, question_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id)

    
def vote(request, question_id):
    return HttpResponse('Voting for %s' % question_id)
