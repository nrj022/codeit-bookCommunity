from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .kyobo import bookInfo

# Create your views here.

def home(request):
    return render(request, 'blog/home.html', {"bookInfo":bookInfo})

def login(request):
    return render(request, 'blog/login.html')

def chatRoom(request):
    return render(request, 'blog/chat-room.html')
