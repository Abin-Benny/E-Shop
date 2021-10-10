from django.shortcuts import render
from django.contrib import messages
from .models import products
# Create your views here.
def index(request):
    if request.method == 'POST':
        mname = request.POST.get('searchname')
        print(mname)
        product = products.objects.filter(product_name=mname)
        if product.count() == 0:
            product = products.objects.all()
            messages.info(request, "Requested product is not available.")
            return render(request, "home.html", {'product': product})
    else:
        product = products.objects.all().order_by('Category__category_name')
    return render(request, "home.html", {'product': product})

def product_details(request,product_slug):
    product = products.objects.get(slug=product_slug)
    context = {'product': product}
    return render(request, "product_details.html", context)






