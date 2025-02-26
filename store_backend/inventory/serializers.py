from rest_framework import serializers
from .models import Shelf
from .models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    shelf = serializers.CharField(max_length=100)

class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ['id', 'name', 'capacity', 'location']  # Asegúrate de incluir location si es necesario