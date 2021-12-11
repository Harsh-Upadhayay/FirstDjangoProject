from django.http.response import HttpResponse
from django.shortcuts import render
import random
from .Music import Music
from .models import song

# Create your views here.

def index(request):
    music = Music()
    songs = list(music.songsList)
    songs = songs[:]
    return render(request, 'index.html', {"songs" : songs})
