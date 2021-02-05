from django.db import models

# Create your models here.
class Sales_table(models.Model):
    sales_item = models.CharField(max_length=30)
    sales_amount = models.CharField(max_length=10)
    sales_date = models.CharField(max_length=10)

    def __str__(self):
        return self.sales_item

class Purchase_table(models.Model):
    purchase_item = models.CharField(max_length=30)
    purchase_amount = models.CharField(max_length=10)
    purchase_date = models.CharField(max_length=10)

    def __str__(self):
        return self.purchase_item        
