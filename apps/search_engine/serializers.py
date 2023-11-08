from rest_framework import serializers
from .models import Searches
from django.urls import reverse

# Serializer para mostrar el listado del las busquedas
class SearchesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Searches
        fields = ('search_text',)
        
        
# Serializer para crear las busquedas
class SearchesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Searches
        fields = ('search_text', 'processed_search_text')