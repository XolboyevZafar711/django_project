from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def hello(request, name):
    return HttpResponse(f"Hello  {name}")

def age(request,name,age):
    return HttpResponse(f"Hello I am {name}, I am {age} years old")

def page(request):
    return render(request, 'index.html')