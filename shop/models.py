from django.db import models

# Create your models here.
from django.shortcuts import render, redirect
from .models import Product, Cart

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    
    # Create or get the user's cart (you can implement this logic based on your user model)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Add the product to the cart
    cart.products.add(product)
    
    return redirect('cart')

def remove_from_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    
    # Get the user's cart
    cart = Cart.objects.get(user=request.user)
    
    # Remove the product from the cart
    cart.products.remove(product)
    
    return redirect('cart')

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=5000, default="")
    
    def __str__(self):
        return self.name
    

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
