from django.shortcuts import render
from apis1.models import SalesTable, PurchaseTable, ListTable
from apis1.serializers import SalesTableSerializer, PurchaseTableSerializer, ListTableSerializer
from rest_framework import viewsets


# Create your views here.
class SalesTableViewSet(viewsets.ModelViewSet):
    queryset = SalesTable.objects.all()
    serializer_class = SalesTableSerializer

class PurchaseTableViewSet(viewsets.ModelViewSet):
    queryset = PurchaseTable.objects.all()
    serializer_class = PurchaseTableSerializer

class ListTableViewSet(viewsets.ModelViewSet):
    queryset = ListTable.objects.all()
    serializer_class = ListTableSerializer    


