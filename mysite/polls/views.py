# 렌더링, 비즈니스 로직
# What to show
# FBVs (Function Based Views) - GET, POST 등을 if문으로 처리해야하는 번거로움

# CBSs (Class Based Views)

from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return HttpResponse("Polls Index View")
    #return HttpResponseRedirect('423/vote')

def detail(request, question_id):
    return HttpResponse("Your Question Id is %s" % question_id)

def results(request, question_id):
    response = "You're looking for the results of question %s" % question_id
    return HttpResponse(response)

def vote(request,question_id):
    return HttpResponse("Voted on Question %s" % question_id)