from django.shortcuts import render

# Create your views here.
def soal(request):
    return render(request, 'soal.html')