from .serializers import HistoryItemCreateSerializer

# Actualiza el historial cuando un usuario entra al detalle de un producto
def update_history(request, product, kwargs):
    user = request.user
    
    if user.is_authenticated:
        history_serializer = HistoryItemCreateSerializer(
            data={
                'history': user.user_history.id, 
                'product': product.id
            }
        )
        history_serializer.is_valid(raise_exception=True)
        history_serializer.save()
        