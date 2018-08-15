from django.http import HttpResponse
from django.shortcuts import render

from .forms import SampleForm


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


def template(request):
    params = {
        "title": "Sample Template",
        "message": "Sample Template Page!",
    }
    return render(request, "sampleapp/sampletmpl.html", params)


def link(request):
    return render(request, "sampleapp/link.html")


def static(request):
    return render(request, "sampleapp/static.html")


def basicform(request):
    params = {
        "message": "What your name?",
    }
    return render(request, "sampleapp/basicform.html", params)


def basicformsubmit(request):
    name = request.POST["name"]
    params = {
        "message": "Hello {0}!".format(name),
    }
    return render(request, "sampleapp/basicform.html", params)


def form(request):
    params = {
        "message": "What your name?",
        "form": SampleForm(),
    }
    if request.method == "POST":
        params["message"] = """Number: {0}
        String: {1}
        Email: {2}
        URL: {3}
        Date: {4}
        Time: {5}
        DateTime: {6}
        Check: {7}
        """.format(
            request.POST["number"],
            request.POST["string"],
            request.POST["email"],
            request.POST["url"],
            request.POST["date"],
            request.POST["time"],
            request.POST["datetime"],
            request.POST["check"],
        )
        params["form"] = SampleForm(request.POST)
    return render(request, "sampleapp/form.html", params)
