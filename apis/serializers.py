# import serializer from rest_framework 
from rest_framework import serializers 

#import the required model to be serialized
from apis.models import Sales_table
from apis.models import Purchase_table

# Create a model serializer  
class SalesSerializer(serializers.HyperlinkedModelSerializer): 
    # specify model and fields 
    class Meta: 
        model = Sales_table 
        fields = ('id', 'sales_item', 'sales_amount', 'sales_date') 

class PurchaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchase_table
        fields= ('id','purchase_item', 'purchase_amount','purchase_date')        
