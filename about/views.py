from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "judul" : "Kelas Terbuka",
        "subjudul" : "tentang Kelas Terbuka",
    }
    return render(request, "about/index.html", context)
