from django.db import models

class StockMovement(models.Model):
    MOVEMENT_TYPES = [
        ('IN', 'Ingreso'),
        ('OUT', 'Salida')
    ]
    product = models.ForeignKey('inventory.Product', on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPES)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.movement_type == 'OUT' and self.product.quantity < self.quantity:
            raise ValueError("No hay suficiente stock disponible")

        if self.movement_type == 'IN':
            self.product.quantity += self.quantity
        else:
            self.product.quantity -= self.quantity

        self.product.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_movement_type_display()} - {self.product.name} ({self.quantity})"
