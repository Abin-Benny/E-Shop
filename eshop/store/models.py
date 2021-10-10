from django.db import models
from category.models import category


# Create your models here.
class products(models.Model):
    product_name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.CharField(max_length=5000)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    Category = models.ForeignKey(category,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.product_name)

