from django.shortcuts import render


# Create your views here.
def index(request):
    """A view that displayes an index page"""
    return render(request, "index.html")


def homepage(request):
    """A view that displayes a home page"""
    return render(request, "home.html")


def aboutUs(request):
    """A view that displayes an about us page"""
    return render(request, "about.html")
