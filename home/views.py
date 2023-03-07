from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Banger awsome project (message written in views.py)")
