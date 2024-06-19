from collections.abc import Iterable
from django.db import models
# Create your models here.
class Payment(models.Model):
    razorpay_payment_id = models.CharField(max_length=250,unique=True)
    razorpay_order_id = models.CharField(max_length=250,unique=True)
    amount = models.CharField(max_length=10)    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

        