from django.shortcuts import render

# Create your views here.
def sellerhome(request):
    return render(request, 'seller templates/sellerhome.html')
def add_product(request):
     return render(request,'seller templates/add_product.html')
def cart(request):
     return render(request,'seller templates/cart.html')
def change_password(request):
     return render(request,'seller templates/change_password.html')
def my_orders(request):
    return render(request,'seller templates/my_orders.html')
def update_stock(request):
     return render(request,'seller templates/update_stock.html')
