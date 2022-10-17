from django.shortcuts import render

# Create your views here.
def materi(request):
    return render(request, 'materi.html')