from django.shortcuts import render

# Create your views here.
def kontak(request):
    return render(request, 'kontak.html')