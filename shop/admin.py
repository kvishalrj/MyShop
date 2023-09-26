from django.contrib import admin

# Register your models here.
from .models import Product # self ***************
from .models import Contact # self ***************

admin.site.register(Product) # self ********************

admin.site.register(Contact) # self ********************
