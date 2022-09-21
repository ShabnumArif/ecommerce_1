from django.urls import path
from . import views


urlpatterns=[
    path('common-index',views.index_page),
    path('',views.seller_login),
    path('customer-login',views.customer_login),
    path('seller-signup',views.seller_signup),
    path('customer-signup',views.customer_signup),
    path('change-password',views.change_password),
    path('image',views.image),
]
