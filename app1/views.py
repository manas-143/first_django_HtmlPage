from django.shortcuts import render
from django.http import HttpResponse


def first(request):
    return HttpResponse("This is my first FVP")

def second(request):
    return HttpResponse("This is my second FVP")

def home(request):
    return render(request,"home.html")

def home1(request):
    return render(request,"home1.html")