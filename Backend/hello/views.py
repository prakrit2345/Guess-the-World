from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world!")

def milan(request):
    return HttpResponse("Hello milan!")


def greet(request, name):
    return HttpResponse(f"Hello,{name}")