from django.shortcuts import render
from django.http import HttpResponse

def httpresponse(request):
    return HttpResponse("Hello!!!")