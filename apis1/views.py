from django.shortcuts import render
from apis1.models import (SalesTable, 
                          PurchaseTable, 
                          ListTable, 
                          PurchaseRequisitionTable,
                          Accept_Reject_Table)
from apis1.serializers import (SalesTableSerializer, 
                               PurchaseTableSerializer, 
                               ListTableSerializer, 
                               PurchaseRequisitionTableSerializer,
                               Accept_Reject_Table_Serializer
                               )
from rest_framework import viewsets, status
from rest_framework.response import Response


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


class PurchaseRequisitionTableViewSet(viewsets.ModelViewSet):
    queryset = PurchaseRequisitionTable.objects.all()
    serializer_class = PurchaseRequisitionTableSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)      
    
    def perform_create(self, serializer):

        # import pdb; pdb.set_trace();
        # import pdb;pdb.set_trace()
        if serializer.validated_data['purchaseAmount']>1000:
            serializer.save()
            return Response({'detail':'WAIT FOR VALIDATION'})
        else:
            print("NO NEED FOR VALIDATION")
            return Response({'detail':'NO NEED FOR VALIDATION'})  

class Accept_Reject_Table_ViewSet(viewsets.ModelViewSet):
    queryset = Accept_Reject_Table.objects.all()
    serializer_class = Accept_Reject_Table_Serializer

  


