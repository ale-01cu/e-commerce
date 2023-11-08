from rest_framework import serializers
from .models import Offer, OfferProduct
from apps.product.serializers import ProductSerializerList

# Serializer de los productos de las ofertas
class OfferProductSerializer(serializers.ModelSerializer):
    product = ProductSerializerList()
    
    class Meta:
        model = OfferProduct
        fields = '__all__'
        
# Seralizer de las ofertas
class OfferSerializer(serializers.ModelSerializer):
    offer_product = OfferProductSerializer(many=True)
    
    class Meta:
        model = Offer
        fields = '__all__'

