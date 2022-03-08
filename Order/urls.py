from django.urls import path
from Order import views

app_name='Order'


urlpatterns=[
    path('add/<pk>/', views.add_to_cart, name="add")
]
