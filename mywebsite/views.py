from django.http import HttpResponse
from django.shortcuts import render

# method untuk menampilkan halaman Home

def index(request):
    context = {
        'judul' : 'kelas terbuka',
        'mentor' : 'faqihza',
        'saya' : 'maulana'
    }
    # method untuk menampilkan beranda web menggunakan file HTML
    return render(request, 'index.html', context)





