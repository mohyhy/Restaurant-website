from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login,authenticate
from .forms import re,log
from main.models import Customer
# Create your views here.

def signup(request):
    if request.method == "POST":
        form = re(request.POST) # to return the same value when user input not valid
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Your sign up success')
            c = Customer(user=user)
            c.save()
            return redirect('login')
        return render(request,"accounts/signup.html",{'form':form})    
    else:
        form = re()
        return render(request,"accounts/signup.html",{'form':form})











def login(request):
    if request.method == "POST":
        form = log(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        if form.is_valid():
            #to check backend if user in model or not
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('index')
            else:
                messages.error(request, 'Invalid username and/or password.')
                return render(request,"accounts/login.html",{'form':form})
                

        
    else:
        form = log()
        return render(request,"accounts/login.html",{'form':form})
