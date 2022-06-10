from django.contrib import admin
from .models import Product, Category, ProductOrder, UserOrder, OrderSatatus
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductOrder)
admin.site.register(UserOrder)
admin.site.register(OrderSatatus)