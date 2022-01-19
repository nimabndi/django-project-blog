from django.shortcuts import render
from django.shortcuts import HttpResponse


def about(request):
    # return HttpResponse('hi there! Im hello world!')
    return render(request, 'about.html')


def home(request):
    # return HttpResponse('Home')
    return render(request, 'home.html')
