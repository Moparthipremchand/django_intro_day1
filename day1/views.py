from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def about(request):
    return HttpResponse("this is about view")

def contact(request):
    return HttpResponse("this is contact view")

def login(request):
    return render(request,"login.html")