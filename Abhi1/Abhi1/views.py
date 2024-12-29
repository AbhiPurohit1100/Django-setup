from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return HttpResponse("hello, saki")

def about(request):
    return HttpResponse("hello, saki, about page")

def name(request):
    return HttpResponse("hello, name page ")

def page(request):
    return render(request, 'website/index.html')