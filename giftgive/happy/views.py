from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    context = {}

    return render(request, 'coolgift/index.html')

def infopage(request):
    context = {}

    return render(request, 'coolgift/infor.html')

def birthpage(request):
    context = {}

    return render(request, 'coolgift/birth.html')
