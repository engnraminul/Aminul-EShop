from django import template
from Order.models import CartToOrder


register = template.Library()

@register.filter
def cart_total(user):
    order = CartToOrder.objects.filter(user=user, allready_ordered=False)

    if order.exists():
        return order[0].orderitems.count()
    else:
        return 0    
