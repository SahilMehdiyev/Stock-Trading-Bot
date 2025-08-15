from django.db import models
from timescale.db.models.fields import TimescaleDateTimeField
from timescale.db.models.managers import TimescaleManager


class Company(models.Model):
    name = models.CharField(max_length=100)
    ticker = models.CharField(max_length=10, unique=True, db_index=True)
    desciption = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)
    timestampt = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



class StockQuote(models.Model):
    """
    'open_price': 131.6,
    'close_price': 131.72,
    'high_price': 131.72,
    'low_price': 131,
    'number_of_trades': 41,
    'volume': 1960,
    'volume_weighted_average': 131.3027,
    'time': datetime.datetime(2023, 8, 15, 8, 0, tzinfo=<UTC>,
    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='stock_quotes')
    open_price = models.DecimalField(max_digits=10, decimal_places=4)
    close_price = models.DecimalField(max_digits=10, decimal_places=4)
    high_price = models.DecimalField(max_digits=10, decimal_places=4)
    low_price = models.DecimalField(max_digits=10, decimal_places=4)
    number_of_trades = models.BigIntegerField(blank=True,null=True)
    volume = models.BigIntegerField()
    volume_weighted_average = models.DecimalField(max_digits=10, decimal_places=4)
    time = TimescaleDateTimeField(interval='1 week',)
    
    objects = models.Manager()
    timescale = TimescaleManager()
    
    
    class Meta:
        unique_together = [('company', 'time')]