from django.db import models
from django.db.models import Avg,Sum,F

# Create your models here.
class Product(models.Model):
    name  = models.CharField()
    category = models.CharField()
    price = models.FloatField()
    stock = models.IntegerField()
    created_at =  models.DateTimeField()

    class Meta:
        pass

def get_all_product():
    return Product.objects.all()

def get_filtered_product(filter):
    query = Product.objects.all()
    if category:=filter.get("category"):
        query.filter(category__iexact=category)
    if mini_price:=filter.get("mini_price"):
        query.filter(price__gte=mini_price)
    if max_price:=filter.get("max_price"):
        query.filter(price__lte=max_price)
    return {
        "total_product" : query.count(),
        "average_price": query.aggregate(avg=Avg("price"))["avg"] or 0,
        "total_stock_value": query.aggregate(
            total=Sum(F("price") * F("stock"))
        )["total"] or 0,
    }