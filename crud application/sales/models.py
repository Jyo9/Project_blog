from django.db import models

# Create your models here.

class SalesData(models.Model):
    region      = models.CharField(max_length=255)
    country     = models.CharField(max_length=100)
    item_type   = models.CharField(max_length=100)
    sales_channel = models.CharField(max_length=100)
    order_priority = models.CharField(max_length=1)
    order_date  = models.DateField()
    order_id    = models.IntegerField(default=None)
    ship_date   = models.DateField()
    units_sold  = models.IntegerField()
    unit_price  = models.FloatField()
    unit_cost   = models.FloatField()
    total_revenue = models.FloatField(blank=True, null=True)
    total_cost  = models.FloatField(blank=True, null=True)
    total_profit= models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ['-id']
