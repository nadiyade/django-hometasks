from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal, Visitor, Ticket, Visit


def index(request):
  #  return HttpResponse("Index page")
    return render(request, 'index.html')


def new(request):
    return render(request, 'first.html')


def final(request):
    return render(request, 'second.html')
    # return HttpResponse("Second page")

def verynew(request):
    return render(request, 'verynew.html')
# Create your views here.

