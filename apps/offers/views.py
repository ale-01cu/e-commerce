from rest_framework import generics
from .serializers import OfferSerializer
from django.db.models import Q
from django.utils import timezone

# Vista para Listar las ofertas activas
class OfferListAPIView(generics.ListAPIView):
    serializer_class = OfferSerializer
    
    def get_queryset(self):
        now = timezone.now()
        return self.get_serializer_class().Meta.model.objects.filter(
            Q(status=True) &
            Q(start_date__lte=now) &
            Q(end_date__gte=now)
        )