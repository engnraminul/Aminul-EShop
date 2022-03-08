from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from Order.models import Cart, CartToOrder
from Shop.models import Product

from django.contrib import messages


@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item = Cart.objects.get_or_create(item=item, user=request.user, allready_purchased=False)
    order_qs = CartToOrder.objects.filter(user=request.user, allready_ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item[0].quantity += 1
            order_item[0].save()
            messages.info(request, "Item quantity was updated")
            return redirect("Shop:home")
        else:
            order.orderitems.add(order_item[0])
            messages.info(request, "Item add your cart")
            return redirect("Shop:home")
    else:
        order = CartToOrder(user=request.user)
        order.save()
        order.orderitems.add(order_item[0])
        messages.info(request, "Item add your cart")
        return redirect("Shop:home")
