from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request,'customer_template/home.html')
def customer_cart(request):
    return render(request,'customer_template/cart.html')
def product_detail(request):
     return render(request,'customer_template/product_detail.html')
def my_orders(request):
     return render(request,'customer_template/my_orders.html')
def change_password(request):
     return render(request,'customer_template/change_password.html')