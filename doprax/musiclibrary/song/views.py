from django.http import HttpResponse
from django.shortcuts import render
from .models import Artist

# Create your views here.
def artist(request):
    artist_list = Artist.objects.all()

    context = {
        'artist_list': artist_list
    }
    return render(request, 'artist.html', context)

def home(request):
    return HttpResponse('This is the home page')

def hello_world(request):
    return HttpResponse('Hello, World!')