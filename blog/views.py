from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'judul' : 'Blog',
        'subjudul' : 'Ini adalah Blog Kelas Terbuka',
    }
    return render(request, 'blog/index.html', context)
    # pass
