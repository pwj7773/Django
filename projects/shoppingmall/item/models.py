from django.db import models
from django.utils import timezone 
# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=100, null=False)
    item_count = models.IntegerField(default=1)

class Order(models.Model):
    item_code = models.ForeignKey(Item,on_delete=models.CASCADE)
    order_date = models.DateTimeField(default=timezone.now,null=False)
    quantity = models.IntegerField(default=1)


