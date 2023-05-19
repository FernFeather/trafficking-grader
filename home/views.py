from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return render(request, 'home/welecome.html', {'today': datetime.today()})
