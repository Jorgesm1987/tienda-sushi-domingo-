from rest_framework import serializers
from .models import Empleado, Cliente, Producto, Carrito, CarritoProducto

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ['run', 'nombres', 'ap_paterno', 'ap_materno', 'email', 'genero', 'region', 'provincia', 'comuna']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'edad', 'telefono', 'email']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'stock']

class CarritoProductoSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()

    class Meta:
        model = CarritoProducto
        fields = ['producto', 'cantidad']

class CarritoSerializer(serializers.ModelSerializer):
    productos = CarritoProductoSerializer(source='carritoproducto_set', many=True)
    cliente = ClienteSerializer()

    class Meta:
        model = Carrito
        fields = ['id', 'cliente', 'productos', 'total']

