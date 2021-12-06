from django.contrib import admin
from .models import prodCategory

class ProductCategory(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display =['name','slug','created_at','updated_at']
    list_filter=['created_at']
    search_fields = ['name']

admin.site.register(prodCategory,ProductCategory)
# Register your models here.
