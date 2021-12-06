from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=True)
    origin_price = models.IntegerField()
    sale_price = models.IntegerField()
    category_id = models.IntegerField()
    status = models.IntegerField()
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    def __str__(self):
       return self.name

class Order(models.Model):
    user_id= models.IntegerField()
    money_total = models.IntegerField()
    user_info=models.TextField()
    status = models.IntegerField()
    payment_method = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

class OrderProduct(models.Model):
    order_id= models.IntegerField()
    product_id= models.IntegerField()
    quality= models.IntegerField()
    sale_price = models.IntegerField()
    money_total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

