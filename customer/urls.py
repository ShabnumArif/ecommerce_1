from django.urls import path
from .import views

urlpatterns=[
    path('home',views.customer_home),
    path('cart',views.customer_cart),
    path('product detail',views.product_detail),
    path('my orders',views.my_orders),
    path('change password',views.change_password),
]