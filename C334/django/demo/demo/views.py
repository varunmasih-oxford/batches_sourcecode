from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("welcome")

def about(request):
    return HttpResponse("Hello all about")

