from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})
    

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "productdetail.html", {"product": product})
    

"""def product_detail(request, pk):
    products = Product.objects.all()
    if pk:
        products = get_object_or_404(Product, pk=pk)
    return render(request, "productdetail.html", {"products": products})"""
    