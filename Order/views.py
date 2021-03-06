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


@login_required
def cart_view(request):
    carts = Cart.objects.filter(user=request.user, allready_purchased=False)
    orders = CartToOrder.objects.filter(user=request.user, allready_ordered=False)
    if carts.exists() and orders.exists():
        order = orders[0]
        return render(request,'order/cart.html', context={'carts':carts, 'order':order})
    else:
        messages.warning(request, "Don't have any items in your cart")
        return redirect("Shop:home")


@login_required
def remove_from_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = CartToOrder.objects.filter(user=request.user, allready_ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, allready_purchased=False)
            order_item = order_item[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request, "item was removed from cart!")
            return redirect("Order:cart")

        else:
            messages.info(request, "This item was not in your cart!")
            return redirect("Shop:home")
    else:
        messages.info(request, "You Don't have an active order")
        return redirect("Shop:home")

@login_required
def increase_quantity(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = CartToOrder.objects.filter(user=request.user, allready_ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, allready_purchased=False)
            order_item = order_item[0]
            if order_item.quantity >=1:
                order_item.quantity +=1
                order_item.save()
                messages.info(request, f"{item.Product_name} quantity has been increase!")
                return redirect("Order:cart")

        else:
            messages.info(request, f"{item.Product_name} is not active in your cart!")
            return redirect("Shop:home")

    else:
        messages.info(request, "You don't have active order!")
        return redirect("Shop:home")


@login_required
def decrease_quantity(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = CartToOrder.objects.filter(user=request.user, allready_ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.orderitems.filter(item=item).exists():
            order_item = Cart.objects.filter(item=item, user=request.user, allready_purchased=False)
            order_item = order_item[0]
            if order_item.quantity >1:
                order_item.quantity -=1
                order_item.save()
                messages.info(request, f"{item.Product_name} quantity has been decrease!")
                return redirect("Order:cart")
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request, f"{item.Product_name} is remove from your cart!")
                return redirect("Order:cart")

        else:
            messages.info(request, f"{item.Product_name} is not active in your cart!")
            return redirect("Shop:home")

    else:
        messages.info(request, "You don't have active order!")
        return redirect("Shop:home")
