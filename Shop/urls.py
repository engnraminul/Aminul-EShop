from django.urls import path
from Shop import views
app_name = 'Shop'

urlpatterns = [
    path('', views.Product_List.as_view(), name='home'),
]
