from rest_framework import serializers

from apis1.models import SalesTable, PurchaseTable, ListTable

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

