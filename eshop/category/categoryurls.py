from django.urls import path
from . import views

urlpatterns=[
    path('<slug:category_slug>/',views.index,name="index_by_category"),

    ]