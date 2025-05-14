from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def get_products(request):
    products = Product.objects.all()
    response = [{"name": p.name, "category": p.category, "price": p.price, "supplier": p.supplier, "rating": p.rating} for p in products]
    return JsonResponse(response, safe=False)