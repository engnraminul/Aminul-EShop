from django.shortcuts import render
from Order.models import CartToOrder
from Payment.models import ShippingAddress
from Payment.forms import ShippingForm

from django.contrib.auth.decorators import login_required

from django.contrib import messages

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
