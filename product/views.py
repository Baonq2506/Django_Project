from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'products/index.html')

def show(request):
    return render(request, 'products/show.html')