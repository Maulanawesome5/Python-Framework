from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul' : 'Halaman Blog',
        'kontributor' : 'ucup',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/blog/cerita', 'Cerita'],
            ['/blog/news', 'News']
        ]
    }
    return render(request, 'blog/index.html', context)

def cerita(request):
    context = {
        'judul' : 'Halaman Cerita',
        'kontributor' : 'otong',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/blog/cerita', 'Cerita'],
            ['/blog/news', 'News']
        ]
    }
    return render(request, 'blog/index.html', context)

def news(request):
    context = {
        'judul' : 'Halaman News',
        'kontributor' : 'sandra bulog',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/blog/cerita', 'Cerita'],
            ['/blog/news', 'News']
        ]
    }
    return render(request, 'blog/index.html', context)
