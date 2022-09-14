from django.urls import path
from . import views



urlpatterns=[
    path('sellerhome', views.sellerhome),
    path('my_orders', views.my_orders),
    path('update_stock',views.update_stock),
    path('add_product',views.add_product),
    path('cart',views.cart),
    path('change password',views.change_password),
]