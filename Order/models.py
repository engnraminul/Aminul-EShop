from django.db import models
from django.conf import settings
from Shop.models import Product
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  related_name="cart")
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    allready_purchased = models.BooleanField(default=False)
    cart_added = models.DateTimeField(auto_now_add=True)
    cart_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} X {self.item}'


    def get_total(self):
        total = self.item.price*self.quantity
        float_total = format(total, '0.2f')
        return float_total


class CartToOrder(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    allready_ordered = models.BooleanField(default=False)
    order_time = models.DateTimeField(auto_now_add=True)
    payment_ID = models.CharField(max_length=264, blank=True, null=True)
    order_ID = models.CharField(max_length=264, blank=True, null=True)


    def get_totals(self):
        total = 0
        for orderitem in self.orderitems.all():
            total += float(orderitem.get_total())
        return total
