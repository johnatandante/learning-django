from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi there, this is my first <b>view</b>")

def detail(request, question_id):
    return HttpResponse('Question %s' % question_id)

    
def results(request, question_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id)

    
def vote(request, question_id):
    return HttpResponse('Voting for %s' % question_id)
