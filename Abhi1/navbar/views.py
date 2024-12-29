from django.shortcuts import render

# Create your views here.
def homenav(request):
    return render(request, 'navbar/first.html')

def size(request):
    return render(request, 'navbar/second.html')