from django.db import models
from django.contrib.auth.models import User
import datetime

class category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_all_categories():
        return category.objects.all()

class item(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200, null=True)
    original_price = models.IntegerField()
    discounted_price = models.IntegerField(null=True)
    description = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to="")
    category = models.ForeignKey(category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
    
    def get_all_items():
        return item.objects.all()

    def get_items_by_categoryID(ID):
        return item.objects.filter(category=ID)
    
    def get_items_by_IDs(IDs):
        return item.objects.filter(id__in=IDs)
    
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(item, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200)
    contact = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def get_orders_by_userid(id):
        return Order.objects.filter(customer=id).order_by('-date')
