from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Kelas Terbuka',
        'heading' : 'Selamat Datang',
        'subheading' : 'di Kelas Terbuka',
        'banner' : 'img/banner_home.png',
    }
    return render(request, 'index.html', context)
