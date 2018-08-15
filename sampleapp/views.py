from django.shortcuts import render
from django.http import HttpResponse

def httpresponse(request):
    return HttpResponse("Hello!!!")

def queryparam(request):
    msg = "nothing"
    if "msg" in request.GET:
        msg = "'{0}'".format(request.GET["msg"])
    return HttpResponse("Message is {0}.".format(msg))

def urlpattern(request, number, text):
    result = "Number: {0}, Text: {1}".format(str(number), text)
    return HttpResponse(result)