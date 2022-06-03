from django.http import HttpResponse
from django.shortcuts import render

# method untuk menampilkan halaman Home

def index(request):
    context = {
        'judul' : 'kelas terbuka',
        'mentor' : 'faqihza mukhlish',
        'salam' : 'selamat datang',
        'nav' : [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/about', 'About'],
            ['/contact', 'Contact']
        ]
    }
    # method untuk menampilkan beranda web menggunakan file HTML
    return render(request, 'index.html', context)





