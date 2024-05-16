from django.db import models
from django.contrib.auth.models import User
from stocks.models import Stock
# Create your models here.
class WatchList(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    stocks = models.ManyToManyField(Stock,related_name="watchlists")

