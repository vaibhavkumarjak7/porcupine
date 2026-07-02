from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def cart_add(request):
    print("Add to cart button clicked")
    return JsonResponse({'Message': 'Add to cart button clicked'})