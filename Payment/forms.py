from django import forms
from Payment.models import ShippingAddress

class ShippingForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address', 'zipcode', 'city', 'country']
