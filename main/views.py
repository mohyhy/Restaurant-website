from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    food = Food.objects.all()
    
    return render(request,'main/index.html',{
        "food":food
    })

def profile(request):
    pass

def cart(request):
    return render(request,'main/cart.html')