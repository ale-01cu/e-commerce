from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()

# Serializer para crear un usuario
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'get_full_name',
            'get_short_name'
        )
        
# Serializer para mostrar el usuario en los comentarios
class UserCommentSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('get_full_name', )
        
     
# Serializer para listar los usuarios
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 
            'email', 
            'first_name', 
            'last_name', 
            'phone_number', 
            'birthdate'
        )
        
# Serializer para actualizar
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')
