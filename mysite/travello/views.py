from django.http.response import HttpResponse
from django.shortcuts import render
import random
# Create your views here.

def index(request):
    return render(request, 'index.html', {'name':chr(int(100*random.random()))})



