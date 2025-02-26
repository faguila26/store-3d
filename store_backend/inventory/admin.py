from django.contrib import admin
from inventory.models import Shelf
from inventory.models import Product

admin.site.register(Shelf)
admin.site.register(Product)
# Register your models here.
