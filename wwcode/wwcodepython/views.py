from django.http import HttpResponse
from django.shortcuts import render
from .models import Event
# Create your views here.
def index(request):
    return render(request,"wwcodepython/index.html")

def applaud(request):
    return HttpResponse("Applaud, Stephanie")

def error(request,name):
    return render(request, "wwcodepython/myerror.html",
    {
        'name':name
    })
def event(request):
    return render(request,'wwcodepython/event.html',
    {
        "events":Event.objects.all()
    }
    )