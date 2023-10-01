from django.contrib import admin

# Register your models here.
from .models import Product, Contact, Orders, OrderUpdate # self ***************

admin.site.register(Product) # self ********************

admin.site.register(Contact) # self ********************

admin.site.register(Orders) # self ********************

admin.site.register(OrderUpdate) # self ********************
