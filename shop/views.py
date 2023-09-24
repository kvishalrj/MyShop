from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return HttpResponse("shop about")

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
