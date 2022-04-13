from django.contrib import admin

# Register your models here.
from .models import Order, Customer, Product, Product_order, Status


admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Product_order)
admin.site.register(Product)
admin.site.register(Status)
