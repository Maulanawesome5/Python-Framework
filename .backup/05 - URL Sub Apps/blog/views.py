from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'blog.html') # method untuk menampilkan blog.html

def recent(request):
    return HttpResponse('<h1>ini adalah halaman Recent Post</h1>')

