from django.shortcuts import render # self *******************
from django.http import HttpResponse # self ****************
from .models import Product # self ************
from math import ceil # self ************

# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlide = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1, nSlide), nSlide])

    # params = {'no_of_slides':nSlide, 'range':range(1,nSlide),'product':products}
    # allProds = [[products, range(1, nSlide), nSlide], [products, range(1, nSlide), nSlide]]

    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("shop contact")

def tracker(request):
    return HttpResponse("shop tracker")

def search(request):
    return HttpResponse("shop search")

def productView(request):
    return HttpResponse("shop productView")

def checkout(request):
    return HttpResponse("shop checkout")
