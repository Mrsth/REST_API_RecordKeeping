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

class PurchaseRequisitionTable(models.Model):

    def validate_PA_Date(value):
        if value <= datetime.now().date():
            pass
        else:
            raise ValidationError('No future dates.')

    purchaseItem = models.CharField(max_length=20, null= True, blank=True) 
    purchaseAmount = models.FloatField(null= True, blank=True)
    purchaseDate = models.DateField(validators=[validate_PA_Date], null= True, blank=True)
    vendorName = models.CharField(max_length=30, null= True, blank=True)
    unitPrice = models.FloatField(null= True, blank=True)
    phoneNo = models.IntegerField(null= True, blank=True)
    approve = models.BooleanField(default=False, null= True, blank=True)
    quantity = models.IntegerField(null= True, blank=True)


    def __str__(self):
        return f"ID = {self.id} Name = {self.purchaseItem} Approve = {self.approve}"

class Accept_Reject_Table(models.Model):
    value = models.BooleanField(default=False)
    key = models.ForeignKey(PurchaseRequisitionTable, on_delete=models.CASCADE, related_name="value")
    


class ListTable(models.Model):
    username = models.CharField(max_length=30)
    content = models.CharField(max_length=100)
    date = models.DateField()

