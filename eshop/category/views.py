from django.shortcuts import render,redirect,get_object_or_404
from category.models import category
from store.models import products

# Create your views here.
def index(request,category_slug=None):

    if category_slug!=None:
        categories = get_object_or_404(category,slug=category_slug)
        product = products.objects.filter(Category=categories)
        return render(request,"home.html", {'product': product})
    else:
        return redirect("index")
