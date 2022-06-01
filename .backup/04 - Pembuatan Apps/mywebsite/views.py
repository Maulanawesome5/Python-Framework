from django.http import HttpResponse
from django.shortcuts import render

# method untuk menampilkan halaman Home

def index(request):
    # method untuk menampilkan beranda web menggunakan file HTML
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')



