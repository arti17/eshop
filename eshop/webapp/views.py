from django.shortcuts import render, get_object_or_404
from .models import Product


def index(request):
    products = Product.objects.order_by('category', 'name').exclude(count=0)
    return render(request, 'index.html', {'products': products})


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail.html', {'product': product})
