from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your models here.

class SalesTable(models.Model):

    def validate_salesDate(value):
        if value <= datetime.now().date():
            pass
        else:
            raise ValidationError('No future dates.')

    salesItem = models.CharField(max_length=30);
    salesAmount = models.IntegerField();
    salesDate = models.DateField(validators=[validate_salesDate])


class PurchaseTable(models.Model):

    def validate_purchaseDate(value):
        if value<=datetime.now().date():
            pass
        else:
            raise ValidationError('No future dates.')

    purchaseItem = models.CharField(max_length=30);
    purchaseAmount = models.IntegerField();
    purchaseDate = models.DateField(validators=[validate_purchaseDate])

class ListTable(models.Model):
    username = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    date = models.DateField()

