from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import SignUpForm


# Product page
def product_page(request,pk):
    product=Product.objects.get(id=pk)
    return render(request, 'productes.html',{'product':product})
# Create your views here.
def home1(request):
    produces=Product.objects.all()
    return render(request, 'home.html',{'productes':productes})


def about_page(request):
    return render(request, 'about.html',{})

def login_page(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("You Have Been Logged In! "))
            return redirect('home')
        else:
            messages.success(request,("You Have Been Logged In! "))
            return redirect('login')
    else:
        return render(request,'login.html')

def logout_page(request):
    logout(request)
    messages.success(request,("You have been logged out... Thenks for stopping... "))
    return redirect('home')

def register_page(request):
    form=SignUpForm()
    if request.method =="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            # log in user
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,("You have registered successfully!! Welcome "))
            return redirect('home')
        else:
            messages.success(request,("Woops! There was a problem Registering, please try again... "))
            return redirect('home')
    else:
        return render(request,'register.html',{'form':form})