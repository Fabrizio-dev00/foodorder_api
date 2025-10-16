from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from .models import Plato, Pedido
from .serializers import PlatoSerializer, PedidoReadSerializer, PedidoWriteSerializer

class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'categoria']


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.prefetch_related('platos').all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['estado', 'platos__nombre']

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return PedidoReadSerializer
        return PedidoWriteSerializer
