from django.contrib import admin
from .models import Categoria, Producto, Proveedor, Etiqueta, DetalleProducto, Cliente, Ventas

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Etiqueta)
admin.site.register(DetalleProducto)
admin.site.register(Cliente)
admin.site.register(Ventas)