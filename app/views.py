from django.shortcuts import render
from .models import *


def home(request):
    return render(request,'index.html')

def categories(request):
    data=Category.objects.all().order_by('-id')
    return render(request, 'categories.html', {'data':data})

def brands(request):
    data=Marca.objects.all().order_by('-id')
    return render(request, 'brands.html', {'data':data})

def products(request):
    data=Product.objects.all().order_by('-id')
    cat=Product.objects.distinct().values('category__title', 'category__id')
    brand=Product.objects.distinct().values('marca__title', 'marca__id')
    color=ProductAttribute.objects.distinct().values('color__title', 'color__color')
    size=ProductAttribute.objects.distinct().values('size__title', 'size__id')
    return render(request, 'products_list.html',
    {
        'data':data,
        'cats':cat,
        'brands':brand,
        'sizes':size,
        'colors':color,
    })


