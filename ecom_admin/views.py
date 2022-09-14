from django.shortcuts import render

# Create your views here.
def admin_login(request):
    return render(request,'ecom_admin templates/admin_login.html')
def home(request):
     return render(request,'ecom_admin templates/home.html')
def approve_sellers(request):
     return render(request,'ecom_admin templates/approve_sellers.html')
def view_sellers(request):
     return render(request,'ecom_admin templates/view_sellers.html')
def view_customers(request):
     return render(request,'ecom_admin templates/view_customers.html')
def view_seller_orders(request):
    return render(request,'ecom_admin templates/view_seller_orders.html')