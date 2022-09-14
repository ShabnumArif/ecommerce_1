from django.urls import path
from . import views



urlpatterns=[
    path('admin', views.admin_login),
    path('home',views.home),
    path('approve sellers',views.approve_sellers),
    path('view sellers',views.view_sellers),
    path('view customers',views.view_customers),
    path('view seller orders',views.view_seller_orders),


]