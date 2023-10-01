from django.shortcuts import render # self *******************
from django.http import HttpResponse # self ****************

# Create your views here.

def index(request):
    return render(request, 'index.html')
