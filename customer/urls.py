from django.urls import path
from . import views
app_name="customer"
urlpatterns=[
    path('home',views.customer_home, name='customer_home'),
    path('cart',views.customer_cart),
    path('product detail',views.product_detail,name='product_detail'),
    path('my orders',views.my_orders),
    path('change password',views.change_password),
    path('new_file',views.new_file),
    path('new1',views.new1),
    path('box',views.box),
]