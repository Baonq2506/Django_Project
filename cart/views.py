from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'carts/index.html')

def heart(request):
    return render(request, 'carts/heart.html')

def checkout(request):
    return render(request, 'carts/checkout.html')

