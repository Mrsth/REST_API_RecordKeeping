from rest_framework import serializers

from apis1.models import (SalesTable, 
                          PurchaseTable, 
                          ListTable,
                          PurchaseRequisitionTable,
                          Accept_Reject_Table)

class SalesTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesTable
        fields = '__all__'

class PurchaseTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseTable
        fields = '__all__'

class ListTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListTable
        fields = '__all__'     

class Accept_Reject_Table_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Accept_Reject_Table
        fields = ["id","value", "key"]

class PurchaseRequisitionTableSerializer(serializers.ModelSerializer):
    value = Accept_Reject_Table_Serializer(many=True, read_only=True)
    class Meta:
        model = PurchaseRequisitionTable
        fields = ['id','purchaseItem', 'purchaseAmount', 'purchaseDate', 
                  'vendorName', 'unitPrice', 'phoneNo', 'approve', 
                  'quantity','value']





