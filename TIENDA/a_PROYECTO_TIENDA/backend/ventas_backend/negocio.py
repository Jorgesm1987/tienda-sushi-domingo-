from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Producto, Cliente, Carrito, CarritoProducto

def procesar_pago(cliente_id, productos):
    try:
        cliente = get_object_or_404(Cliente, id=cliente_id)
        productos_comprados = []

        for prod in productos:
            producto = get_object_or_404(Producto, id=prod['id'])
            if producto.stock < prod['cantidad']:
                return JsonResponse({'status': 'Stock insuficiente para el producto: ' + producto.nombre}, status=400)
            producto.stock -= prod['cantidad']
            producto.save()
            productos_comprados.append({
                'id': producto.id,
                'nombre': producto.nombre,
                'cantidad': prod['cantidad']
            })

        # Lógica adicional para guardar la compra en la base de datos, si es necesario
        # Ejemplo: registrar la compra en un modelo de historial de compras
        # HistorialCompra.objects.create(cliente=cliente, productos=productos_comprados, total=calcular_total(productos_comprados))

        return {'status': 'Compra procesada exitosamente', 'productos': productos_comprados}
    except Producto.DoesNotExist:
        return JsonResponse({'status': 'Producto no encontrado'}, status=404)
    except Cliente.DoesNotExist:
        return JsonResponse({'status': 'Cliente no encontrado'}, status=404)

def calcular_total(productos):
    total = sum(prod['precio'] * prod['cantidad'] for prod in productos)
    return total
