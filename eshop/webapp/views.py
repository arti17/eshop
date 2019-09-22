from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, category_choices
from .forms import ProductForm, SearchForm


def get_categories():
    products = Product.objects.exclude(count=0)
    categories = []
    for product in products:
        category = str(product).split('-')
        if category[1].strip() not in categories:
            categories.append(category[1].strip())
    return categories


def index(request):
    form = SearchForm()
    products = Product.objects.order_by('category', 'name').exclude(count=0)
    categories = get_categories()
    return render(request, 'index.html', {'products': products, 'categories': categories, 'form': form})


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'detail.html', {'product': product})


def create(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create.html', {'statuses': category_choices, 'form': form})

    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                count=form.cleaned_data['count'],
                price=form.cleaned_data['price']
            )
            return redirect('index')
        else:
            return render(request, 'create.html', context={'form': form})


def update(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'GET':
        form = ProductForm(data={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'count': product.count,
            'price': product.price
        })
        return render(request, 'update.html', context={'form': form, 'product': product})

    if request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.name = form.cleaned_data['name']
            product.description = form.cleaned_data['description']
            product.category = form.cleaned_data['category']
            product.count = form.cleaned_data['count']
            product.price = form.cleaned_data['price']
            product.save()
            return redirect('index')
        else:
            return render(request, 'update.html', context={'form': form, 'task': product})


def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')


def filter_by_category(request, category):
    products = Product.objects.filter(category=category).exclude(count=0).order_by('name')
    categories = get_categories()
    return render(request, 'filtered_page_by_category.html', {'products': products, 'categories': categories, 'category': category})


def search(request):
    categories = get_categories()
    form = SearchForm(data=request.GET)
    if form.is_valid():
        name = form.cleaned_data['name']
        products = Product.objects.filter(name__contains=name)
        return render(request, 'index.html', {'products': products, 'categories': categories, 'form': form})
    else:
        return redirect('index')
