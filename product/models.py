from turtle import ondrag
from django.db import models
from user.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table= 'category'
    category_name = models.CharField(max_length=128)

class Product(models.Model):
    class Meta:
        db_table= 'product'
    product_name = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    desc = models.TextField()
    price = models.CharField(max_length=128)
    quantity = models.CharField(max_length=128)


class OrderSatatus(models.Model):
    status_name = models.CharField(max_length=128)

class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.CharField(max_length=128)
    order_time = models.DateTimeField()
    price = models.CharField(max_length=128)
    discount_per = models.CharField(max_length=128)
    last_price = models.CharField(max_length=128)
    is_valid = models.BooleanField(default=True)
    order_status = models.ForeignKey(OrderSatatus, default=1,on_delete=models.CASCADE)

class ProductOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.CharField(max_length=128)
    user_order = models.ForeignKey(UserOrder, on_delete=models.CASCADE)