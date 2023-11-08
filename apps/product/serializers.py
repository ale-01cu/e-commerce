from rest_framework import serializers
from .models import Product, Image, Measure_unit, Brand

# Serializer de las Marcas
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('name',)

# Serializer de las Unidades de Medida
class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure_unit
        fields = ('name', 'symbol')
        
# Serializer de las Imágenes
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('url', )
        
# Serializer para el detalle de los Productos
class ProductSerializerDetail(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    Images = ImageSerializer(many=True)
    measure_unit = MeasureUnitSerializer()
    brand = BrandSerializer()
    rating = serializers.SerializerMethodField()
    discount_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def get_rating(self, obj):
        return obj.rating
        
    def get_discount_price(self, obj):
        return obj.discount_price
    
        
# Serializeer para listar los productos       
class ProductSerializerList(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    discount_price = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    description=serializers.StringRelatedField()
    class Meta:
        model = Product
        exclude = (
            'stock', 
            'measure_unit', 
            'keywords', 
            'brand',
            'create_date',
            'status'
        )
        
    def get_discount_price(self, obj):
        return obj.discount_price
    
    def get_rating(self, obj):
        return obj.rating
        
        