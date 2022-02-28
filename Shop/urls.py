from django.urls import path
from Shop import views
app_name = 'Shop'

urlpatterns = [
    path('', views.Product_List.as_view(), name='home'),
    path('detail/<pk>/', views.ProductDetail.as_view(), name='detail')
]
