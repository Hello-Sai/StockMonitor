from django.db import models

# Create your models here.
class Stock(models.Model):
    symbol = models.CharField(unique=True,max_length=25)
    timestamp = models.DateTimeField()
    low = models.CharField(max_length=10)
    high = models.CharField(max_length=10)
    close = models.CharField(max_length=10)
    timezone = models.CharField(max_length=25)
    volume = models.CharField(max_length=4)
    open = models.CharField(max_length=10)

    @property
    def amount(self):
        self.high -100