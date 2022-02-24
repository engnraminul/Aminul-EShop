from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from Shop.models import Product

class Product_List(ListView):
    model = Product
    template_name = 'Shop/home.html'
