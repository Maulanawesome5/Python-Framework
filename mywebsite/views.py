from django.shortcuts import render

def index(request):
    context = {
        'judul':'Kelas Terbuka',
        'subjudul':'Selamat Datang',
    }
    return render(request, template_name="index.html", context=context)

