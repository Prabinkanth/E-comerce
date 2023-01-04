from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages         
# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
     products = Product.objects.all()
     return render(request,'home.html',{'products':products})

def shop(request):
     return render(request,'shop.html')

def contact(request):
     return render(request,'contact.html')

def signup(request):
     username=request.POST.get('username')
     password=request.POST.get('password')

     if request.method=='POST':
          user = authenticate(username=username,password=password)
          if user is not None:
               login(request,user)
               return redirect('home:home')

          else:
               messages.error(request,'user not exist')
               return redirect('home:signup')

     return render(request,'login.html')

def logout_user(request):
     logout(request)
     return redirect('home:home')

