from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'internet_shop/index.html')


def internet_shop(request):
    return render(request, 'internet_shop/internet_shop.html')