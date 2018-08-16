from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.paginator import Paginator

from .forms import SampleForm, SampleModelForm
from .models import SampleModel


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


def list(request):
    data = SampleModel.objects.all()
    params = {
        "message": "",
        "data": data,
    }
    return render(request, "sampleapp/list.html", params)


def create(request):
    if request.method == "POST":
        item = SampleModel()
        form = SampleModelForm(request.POST, instance=item)
        form.save()
        return redirect(to="/sampleapp/list")
    params = {
        "message": "",
        "form": SampleModelForm(),
        "button_txt": "Create",
    }
    return render(request, "sampleapp/edit.html", params)


def update(request, id):
    item = SampleModel.objects.get(id=id)
    if request.method == "POST":
        form = SampleModelForm(request.POST, instance=item)
        form.save()
        return redirect(to="/sampleapp/list")
    params = {
        "message": "",
        "id": id,
        "form": SampleModelForm(instance=item),
        "button_txt": "Update",
    }
    return render(request, "sampleapp/edit.html", params)

def delete(request, id):
    item = SampleModel.objects.get(id=id)
    item.delete()
    return redirect(to="/sampleapp/list")
    

def listpaging(request, page=1):
    data = SampleModel.objects.all()
    paginator = Paginator(data, 5)
    params = {
        "message": "",
        "data": paginator.get_page(page),
    }
    return render(request, "sampleapp/listpaging.html", params)
