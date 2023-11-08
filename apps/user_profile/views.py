from .serializers import UserProfileListSerializer, UserProfileUpdateSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError
User = get_user_model()
    
    
class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return UserProfileListSerializer.Meta.model.objects.filter(user__is_active=True)
    
    # Devuelve el perfil del usuario que realiza la peticion
    def get(self, request):
        try:
            user = request.user  
            queryset = self.get_queryset()      
            profile = get_object_or_404(queryset, user=user)
            serializer = UserProfileListSerializer(profile)
            
            return Response(
                serializer.data, 
                status=status.HTTP_200_OK
            )
        
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Server internal error'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    # Actualiza el perfil del usuario que realiza la peticion con los datos que envie
    def put(self, request):
        try:
            user = request.user
            queryset = self.get_queryset() 
            profile = get_object_or_404(queryset, user=user)
            serializer = UserProfileUpdateSerializer(
                instance=profile, 
                data=request.data
            )
                    
            if serializer.is_valid():
                serializer.save()
                
                return Response(
                    serializer.data, 
                    status=status.HTTP_200_OK
                )
            
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        except IntegrityError:
            return Response(
                {'error': f'User {user.email} already exists'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        except Exception as e:
            print(type(e))
            return Response(
                {'error': 'Server internal error'}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    