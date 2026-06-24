from django.shortcuts import render
from .models import Product
# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'store/index.html',{'products':products})

def detail(request,slug):
    product = Product.objects.get(slug=slug)
    return render(request,'store/detail.html',{'product': product})