from apps.comments.models import Comments
from rest_framework import serializers

# Serializer para listar los comentarios de un producto
class CommentsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        exclude = ('status', 'product')    
        
    def to_representation(self, instance):       
        return {
            'id': instance.id,
            'rating': instance.rating,
            'comment': instance.comment,
            'user': instance.user.first_name
        }
    
# Serializer para crear y actualizar los comentarios
class CommentsSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Comments
        exclude = ('user',)
        
    def validate_rating(self, data):
        if data < 0 or data > 5:
            raise serializers.ValidationError({'error': 'Rating invalido'})
        return super().validate(data)
        