from rest_framework import serializers
from .models import UserProfile
from apps.user.serializers import UserUpdateSerializer, UserListSerializer
from drf_writable_nested.serializers import WritableNestedModelSerializer
        
# Serializer para mostrar la info del perfil
class UserProfileListSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True)
    
    class Meta:
        model = UserProfile
        fields = '__all__'
        

# Serializer para actualizar la info del perfil 
class UserProfileUpdateSerializer(WritableNestedModelSerializer):
    user = UserUpdateSerializer()
    
    class Meta:
        model = UserProfile
        fields = '__all__'




