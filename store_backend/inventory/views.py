from rest_framework import viewsets
from .models import Product, Shelf, StockMovement  
from .serializers import ProductSerializer, ShelfSerializer, StockMovementSerializer

# Vista para Product
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Obtiene todos los productos
    serializer_class = ProductSerializer  # Usa el serializador que definiste

# Vista para Shelf
class ShelfViewSet(viewsets.ModelViewSet):
    queryset = Shelf.objects.all()  # Obtiene todas las estanterías
    serializer_class = ShelfSerializer  # Usa el serializador para las estanterías

# Vista para StockMovement
class StockMovementViewSet(viewsets.ModelViewSet):
    queryset = StockMovement.objects.all().order_by('-timestamp')
    serializer_class = StockMovementSerializer
