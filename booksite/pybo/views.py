from django.shortcuts import render
from .kyobo import bookInfo

# Create your views here.

def home(request):
    return render(request, 'pybo/home.html', {"bookInfo":bookInfo})
