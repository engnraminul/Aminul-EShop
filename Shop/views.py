from django.shortcuts import render
from django.views.generic import ListView, DetailView
# Create your views here.
from Shop.models import Product
#LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class Product_List(ListView):
    model = Product
    template_name = 'Shop/home.html'


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'shop/product_detail.html'
