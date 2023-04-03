from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view for returning index page """
    return render(request, 'home/index.html')