from django.shortcuts import render,redirect
from store.models import products
# Create your views here.
def logincheck(request,product_id):
    if request.user.is_authenticated:
        product = products.objects.filter(id=product_id)
        return render(request,"cart.html",{'product':product})
    else:
        return redirect("login")

def checkout(request,price):
    if request.method == 'POST':
        numb = request.POST.get('num')

        sum =int(numb)*int(price)

        return render(request,"checkout.html",{'sum':sum,'price':price,'num':numb})
