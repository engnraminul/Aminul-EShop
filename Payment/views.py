from django.shortcuts import render, HttpResponseRedirect, redirect
from Order.models import CartToOrder
from Payment.models import ShippingAddress
from Payment.forms import ShippingForm

from django.contrib.auth.decorators import login_required

from django.contrib import messages
import requests

#payment
import requests
#from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket

@login_required
def checkout(request):
    saved_address = ShippingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = ShippingForm(instance=saved_address)
    if request.method == "POST":
        form = ShippingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = ShippingForm(instance=saved_address)
            messages.info(request, "Your Address in saved!")

    order_qs = CartToOrder.objects.filter(user=request.user, allready_ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_total = order_qs[0].get_totals()

    return render(request, 'Payment/checkout.html', context={"form":form, "order_items":order_items, "order_total":order_total, "saved_address":saved_address})


@login_required
def payment(request):
    saved_address = ShippingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    if not saved_address.is_fully_filled():
        messages.info(request, f"please complete Shipping address form!")
        return redirect("Payment:checkout")

    if not request.user.profile.is_fully_fillup():
        messages.info(request, f"please complete your profile details!")
        return redirect("Login:profile")
    return render(request, "Payment/payment.html")
