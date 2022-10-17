from django.shortcuts import render

# Create your views here.
def beranda(request):
    judul = "Beranda"

    konteks = {
        'title': judul
    }
    return render(request, 'beranda.html')