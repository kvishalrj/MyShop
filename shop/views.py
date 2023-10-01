from django.shortcuts import render # self *******************
from django.http import HttpResponse # self ****************
from .models import Product, Contact, Orders, OrderUpdate # self ************

from math import ceil # self ************

import json

# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    # print(cats)
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
    if request.method=="POST":
        name = request.POST.get('name'," ")
        email = request.POST.get('email'," ")
        phone = request.POST.get('phone'," ")
        desc = request.POST.get('desc'," ")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId'," ")
        email = request.POST.get('email'," ")
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp})
                    response = json.dumps(updates, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    # Fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/prodView.html', {'product':product[0]})

def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson'," ")
        name = request.POST.get('name'," ")
        email = request.POST.get('email'," ")
        address = request.POST.get('address1'," ") + request.POST.get('address2'," ")
        state = request.POST.get('state'," ")
        city = request.POST.get('city'," ")
        zip_code = request.POST.get('zip_code'," ")
        phone = request.POST.get('phone'," ")

        order = Orders(items_json=items_json, name=name, email=email, address=address, state=state, city=city, zip_code=zip_code, phone=phone)

        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id

        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})

    return render(request, 'shop/checkout.html')
