from django.urls import path
from . import views

urlpatterns=[
    path('addcart/<int:product_id>/',views.logincheck,name="logincheck"),
    path('Checkout/<int:price>/', views.checkout, name="checkout"),

    ]