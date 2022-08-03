from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "judul" : "Kelas Terbuka",
        "subjudul" : "tentang Kelas Terbuka",
        "banner" : "about/img/banner_about.png",
        "app_css" : "about/css/style.css",
    }
    return render(request, "index.html", context)
