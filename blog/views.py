from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul' : 'ini halaman Blog',
        'mentor' : 'ucup'
    }
    return render(request, 'blog/index.html', context)

def news(request):
    context = {
        'judul' : 'ini halaman News',
        'mentor' : 'otong'
    }
    return render(request, 'blog/index.html', context)

def cerita(request):
    context = {
        'judul' : 'ini halaman Cerita',
        'mentor' : 'sandra bulog'
    }
    return render(request, 'blog/index.html', context)


