from django.http.response import HttpResponse
from django.shortcuts import render
import random
# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':chr(int(100*random.random()))})

def add(request):
    sum = int(request.POST["a"]) + int(request.POST["b"])
    return render(request, 'summation.html', {'sum': sum})