from django.urls import path
from . import views

app_name = "cart"
urlpatterns = [
    path('',views.index,name='index'),
    path('heart',views.heart,name='cart_heart'),
    path('checkout',views.checkout,name='checkout'),

]
