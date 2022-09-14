from django.shortcuts import render

# Create your views here.

def index_page(request):
    return render(request,'common_templates/index.html')

def seller_login(request):
        return render(request,'common_templates/seller_login.html')

def customer_login(request):
        return render(request,'common_templates/customer_login.html')
def seller_signup(request):
        return render(request,'common_templates/seller_signup.html')
def customer_signup(request):
        return render(request,'common_templates/customer_signup.html')
def change_password(request):
        return render(request,'common_templates/change_password.html')
def image(request):
        return render(request,'common_templates/image.html')

