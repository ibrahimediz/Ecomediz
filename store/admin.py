from django.contrib import admin

admin.site.site_header = "My Store"
admin.site.site_title = "My Store"
admin.site.index_title = "Welcome to My Store"

from .models.Category import Category
from .models.Customers import Customer
from .models.Products import Products
from .models.Orders import Order


admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
