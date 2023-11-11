from django.shortcuts import render
from internet_shop.models import ProductCategory, Product


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'internet_shop/index.html', context=context)


def internet_shop(request):
    context = {
        'title': 'Store - catalog',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'internet_shop/internet_shop.html', context=context)