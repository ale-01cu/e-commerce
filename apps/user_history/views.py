from rest_framework.response import Response
from rest_framework import status, views
from .serializers import HistorySerializer
from rest_framework.permissions import IsAuthenticated

# Devuelve el historial del usuario que realiza la peticion
class HIstoryAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            user = request.user
            user_history = user.user_history
            history_serializer = HistorySerializer(user_history)
            
            return Response(
                history_serializer.data,
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            print(e)
            return Response(
                {'error': 'Something went wrong when adding item to cart'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

