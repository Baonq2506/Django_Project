from django.shortcuts import render

# Page home.
def index(request):
    return render(request, 'index.html')



