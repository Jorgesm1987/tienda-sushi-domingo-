from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Empleado, Cliente, Carrito, CarritoProducto, Producto, Pedido, DetallePedido, Pago, Direccion
from .serializers import EmpleadoSerializer, ClienteSerializer, ProductoSerializer, CarritoSerializer, CarritoProductoSerializer
import json
from .negocio import procesar_pago, calcular_total

@csrf_exempt
def create_empleado(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        empleado = Empleado.objects.create(
            run=data['run'],
            nombres=data['nombres'],
            ap_paterno=data['ap_paterno'],
            ap_materno=data['ap_materno'],
            email=data['email'],
            genero=data['genero'],
            region=data['region'],
            provincia=data['provincia'],
            comuna=data['comuna']
        )
        return JsonResponse({'success': True, 'message': 'Empleado creado exitosamente'}, status=201)

@csrf_exempt
def read_empleado(request, run):
    try:
        empleado = Empleado.objects.get(run=run)
        empleado_data = {
            'run': empleado.run,
            'nombres': empleado.nombres,
            'ap_paterno': empleado.ap_paterno,
            'ap_materno': empleado.ap_materno,
            'email': empleado.email,
            'genero': empleado.genero,
            'region': empleado.region,
            'provincia': empleado.provincia,
            'comuna': empleado.comuna
        }
        return JsonResponse(empleado_data, status=200)
    except Empleado.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Empleado no encontrado'}, status=404)

@csrf_exempt
def update_empleado(request, run):
    if request.method == 'PUT':
        try:
            empleado = Empleado.objects.get(run=run)
            data = json.loads(request.body)
            empleado.nombres = data['nombres']
            empleado.ap_paterno = data['ap_paterno']
            empleado.ap_materno = data['ap_materno']
            empleado.email = data['email']
            empleado.genero = data['genero']
            empleado.region = data['region']
            empleado.provincia = data['provincia']
            empleado.comuna = data['comuna']
            empleado.save()
            return JsonResponse({'success': True, 'message': 'Empleado actualizado exitosamente'}, status=200)
        except Empleado.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Empleado no encontrado'}, status=404)

@csrf_exempt
def delete_empleado(request, run):
    if request.method == 'DELETE':
        try:
            empleado = Empleado.objects.get(run=run)
            empleado.delete()
            return JsonResponse({'success': True, 'message': 'Empleado eliminado exitosamente'}, status=200)
        except Empleado.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Empleado no encontrado'}, status=404)

@csrf_exempt
def create_cliente(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cliente = Cliente.objects.create(
            rut=data['rut'],
            nombre=data['nombre'],
            edad=data['edad'],
            telefono=data['telefono'],
            email=data['email']
        )
        return JsonResponse({'success': True, 'message': 'Cliente creado exitosamente'}, status=201)

@csrf_exempt
def read_cliente(request, rut):
    try:
        cliente = Cliente.objects.get(rut=rut)
        cliente_data = {
            'rut': cliente.rut,
            'nombre': cliente.nombre,
            'edad': cliente.edad,
            'telefono': cliente.telefono,
            'email': cliente.email
        }
        return JsonResponse(cliente_data, status=200)
    except Cliente.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Cliente no encontrado'}, status=404)

@csrf_exempt
def update_cliente(request, rut):
    if request.method == 'PUT':
        try:
            cliente = Cliente.objects.get(rut=rut)
            data = json.loads(request.body)
            cliente.rut = data['rut']
            cliente.nombre = data['nombre']
            cliente.edad = data['edad']
            cliente.telefono = data['telefono']
            cliente.email = data['email']
            cliente.save()
            return JsonResponse({'success': True, 'message': 'Cliente actualizado exitosamente'}, status=200)
        except Cliente.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Cliente no encontrado'}, status=404)

@csrf_exempt
def delete_cliente(request, rut):
    if request.method == 'DELETE':
        try:
            cliente = Cliente.objects.get(rut=rut)
            cliente.delete()
            return JsonResponse({'success': True, 'message': 'Cliente eliminado exitosamente'}, status=200)
        except Cliente.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Cliente no encontrado'}, status=404)

@csrf_exempt
def procesar_pago_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cliente_id = data.get('cliente_id')
        productos = data.get('productos')
        direccion_entrega_id = data.get('direccion_entrega_id')
        metodo_pago = data.get('metodo_pago')
        
        # Crear el pedido
        cliente = get_object_or_404(Cliente, id=cliente_id)
        direccion_entrega = get_object_or_404(Direccion, id=direccion_entrega_id)
        pedido = Pedido.objects.create(
            cliente=cliente,
            direccion_entrega=direccion_entrega,
            total=calcular_total(productos)
        )

        # Crear los detalles del pedido
        for prod in productos:
            producto = get_object_or_404(Producto, id=prod['id'])
            DetallePedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=prod['cantidad'],
                precio=producto.precio
            )
            producto.stock -= prod['cantidad']
            producto.save()

        # Registrar el pago
        Pago.objects.create(
            pedido=pedido,
            monto=pedido.total,
            metodo_pago=metodo_pago
        )

        # Redireccionar a la vista de comprobante de boleta
        return HttpResponseRedirect(f'/api/comprobante/{pedido.id}/')

    return JsonResponse({'status': 'Método no permitido'}, status=405)

# def comprobante_boleta(request, pedido_id):
#     pedido = get_object_or_404(Pedido, id=pedido_id)
#     detalles = DetallePedido.objects.filter(pedido=pedido)
#     pago = Pago.objects.get(pedido=pedido)
#     return render(request, 'comprobante.html', {
#         'pedido': pedido,
#         'detalles': detalles,
#         'pago': pago
#     })

def pagar(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cliente_id = data.get('cliente_id')
        productos = data.get('productos')
        direccion_entrega_id = data.get('direccion_entrega_id')
        metodo_pago = data.get('metodo_pago')

        # Crear el pedido
        cliente = get_object_or_404(Cliente, id=cliente_id)
        direccion_entrega = get_object_or_404(Direccion, id=direccion_entrega_id)
        pedido = Pedido.objects.create(
            cliente=cliente,
            direccion_entrega=direccion_entrega,
            total=calcular_total(productos)
        )

        # Crear los detalles del pedido
        for prod in productos:
            producto = get_object_or_404(Producto, id=prod['id'])
            DetallePedido.objects.create(
                pedido=pedido,
                producto=producto,
                cantidad=prod['cantidad'],
                precio=producto.precio
            )
            producto.stock -= prod['cantidad']
            producto.save()

        # Registrar el pago
        Pago.objects.create(
            pedido=pedido,
            monto=pedido.total,
            metodo_pago=metodo_pago
        )

        # Redireccionar a la vista de comprobante de boleta
        return HttpResponseRedirect(f'/api/comprobante/{pedido.id}/')
    return render(request, 'pagar.html')


def comprobante_boleta(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    detalles = DetallePedido.objects.filter(pedido=pedido)
    pago = Pago.objects.get(pedido=pedido)
    return render(request, 'comprobante.html', {
        'pedido': pedido,
        'detalles': detalles,
        'pago': pago
    })

