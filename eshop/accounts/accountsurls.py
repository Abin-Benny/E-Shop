from django.urls import path
from . import views

urlpatterns=[
    path('Register/',views.user_register,name="register"),
    path('Login/', views.user_login, name="login"),
    path('Logout/', views.user_logout, name="logout"),
    ]