from django.shortcuts import render
from .models import Product
from .models import Category
# Create your views here.

def Product_list(request):
  products = Product.objects.all()
  categories = Category.objects.all()
  return render(request, 'products/product_list.html', {
    'products':products,
    'categories':categories
    })