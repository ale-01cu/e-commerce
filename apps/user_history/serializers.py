from rest_framework import serializers
from .models import History, HistoryItem
from apps.product.serializers import ProductSerializerList

# Serializer del modelo que contiene los productos de cada historial solo para listar los datos
class HistoryItemListSerializer(serializers.ModelSerializer):
    product = ProductSerializerList(read_only=True)
    
    class Meta:
        model = HistoryItem
        exclude = ('history',)


# Serializer del historial
class HistorySerializer(serializers.ModelSerializer):
    history_products = HistoryItemListSerializer(
        many=True, 
        read_only=True
    )

    class Meta:
        model = History
        fields = ('history_products',)

    # Devuelve los productos del historial limitados
    def to_representation(self, instance):
        data = super().to_representation(instance)
        
        return {
            'history_products': data['history_products'][:10]
        }