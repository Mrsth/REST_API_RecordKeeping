from django.shortcuts import render
from rest_framework import viewsets


#Import models and its serializer
from apis.models import Sales_table, Purchase_table
from apis.serializers import SalesSerializer
from apis.serializers import PurchaseSerializer

# Create your views here.
class SalesViewSet(viewsets.ModelViewSet): 
    # define queryset 
    queryset = Sales_table.objects.all() 
      
    # specify serializer to be used 
    serializer_class = SalesSerializer 

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase_table.objects.all()
    serializer_class = PurchaseSerializer  
