from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'home/homepage.html')
    # return HttpResponse("<h1>Hello World !!!</h1> Jenking is Working??")
# Create your views here.
