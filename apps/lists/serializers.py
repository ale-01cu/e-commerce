from rest_framework import serializers
from apps.product.models import Product
from .models import CustomsList, CustomsListItem
from apps.product.serializers import ProductSerializerList
        
class CustomListItemSerializer(serializers.ModelSerializer):
    product = ProductSerializerList(read_only=True)
    
    class Meta:
        model = CustomsListItem
        fields = ('product',)

class CustomListsSerializer(serializers.ModelSerializer):
    custom_list_items = CustomListItemSerializer(
        many=True, 
        read_only=True
    )
    
    class Meta:
        model = CustomsList
        fields = ('name', 'custom_list_items')
        


