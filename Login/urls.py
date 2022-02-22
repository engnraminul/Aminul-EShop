from django.urls import path
from Login import views

app_name = 'Login'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]
