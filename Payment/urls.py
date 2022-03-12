from django.urls import path
from Payment import views

app_name = "Payment"

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
    path('pay/', views.payment, name="payment"),
]
