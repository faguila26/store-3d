from rest_framework import viewsets
from .models import Product, Shelf  # Asegúrate de que estos modelos estén importados
from .serializers import ProductSerializer, ShelfSerializer  # Asegúrate de que estos serializadores estén importados


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Obtiene todos los productos
    serializer_class = ProductSerializer  # Usa el serializador que definiste

# Vista para Shelf
class ShelfViewSet(viewsets.ModelViewSet):
    queryset = Shelf.objects.all()  # Obtiene todas las estanterías
    serializer_class = ShelfSerializer  # Usa el serializador para las estanterías
