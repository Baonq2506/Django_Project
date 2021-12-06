from django.contrib import admin
from django.contrib import admin
from .models import Order, OrderProduct, Product
from .models import Order
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display =['name','content','origin_price','sale_price','created_at','updated_at']
    list_filter=['created_at']
    search_fields = ['name']

class OrderAdmin(admin.ModelAdmin):
    list_display =['user_id','money_total','status','payment_method','created_at','updated_at']
    list_filter=['created_at']
    search_fields = ['name']

class OrderProductAdmin(admin.ModelAdmin):
    list_display =['order_id','product_id','quality','sale_price','money_total','created_at','updated_at']
    list_filter=['created_at']
    search_fields = ['name']

admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)