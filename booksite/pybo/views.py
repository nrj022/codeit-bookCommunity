from django.shortcuts import render
from .kyobo import books

# Create your views here.

def home(request):
    return render(request, 'pybo/home.html', {"books":books})

def kyoboDetail(request, id):
    return render(request, 'pybo/chat-room.html')
