from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request,'customertemplate/home.html')
def customer_cart(request):
    return render(request,'customertemplate/cart.html')
def product_detail(request):
     return render(request,'customertemplate/product_detail.html')
def my_orders(request):
     return render(request,'customertemplate/my_orders.html')
def change_password(request):
     return render(request,'customertemplate/change_password.html')
def new_file(request):
      return render(request,'customertemplate/new_file.html')
def new1(request):
      return render(request,'customertemplate/new1.html')  
def box(request):
      return render(request,'customertemplate/box.html')