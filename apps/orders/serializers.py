from .models import Order,OrderItem
from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from apps.product.models import Product    

# Serializa el modelo de los items de las ordenes para listar una orden
class OrderItemSerializerList(serializers.ModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        read_only=True, 
        view_name='product-detail'
    )
    
    class Meta():
        model = OrderItem
        exclude = ('order',)
        
# Serializa el modelo de los items de las ordenes para crear una orden
class OrderItemSerializerCreate(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.filter(stock__gt=0))
    
    class Meta():
        model = OrderItem
        exclude = ('order',)
        
# Serializa el modelo de las ordenes para listar una orden
class OrderSerializerList(serializers.ModelSerializer):
    class Meta():
        model = Order
        fields = '__all__'
        
# Serializa el modelo de las ordenes para crear una orden
class OrderSerializerDetail(WritableNestedModelSerializer):
    order_items = OrderItemSerializerList(many=True)
    amount = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()
    
    class Meta():
        model = Order
        exclude = ('user',)
        
    def get_amount(self, obj):
        return obj.amount
    
    def get_total_price(self, obj):
        return obj.total_price
        
# Serializa el modelo de las ordenes para crear una orden
class OrderSerializerCreate(WritableNestedModelSerializer):
    order_items = OrderItemSerializerCreate(many=True)
    
    class Meta():
        model = Order
        exclude = (
            'user', 
            'order_number', 
        )
        
    def validate_order_items(self, value):
        if len(value) == 0:
            raise serializers.ValidationError({
                'error': 'Order items is required'})
        
        for order_item in value:
            if order_item['count'] <= 0:
                raise serializers.ValidationError({
                    'error': f'The count of { order_item["product"].name } is required.'})
            if order_item['product'].stock < order_item['count']:
                raise serializers.ValidationError({
                    'error': f'There is no { order_item["count"] } { order_item["product"].name } available in the warehouse.'})
        return super().validate(value)
    
    
    def validate_phone_number(self, value):
        if len(value) == 0:
            raise serializers.ValidationError({
                'error': 'Phone number is required'})
        return super().validate(value)
    
    
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)