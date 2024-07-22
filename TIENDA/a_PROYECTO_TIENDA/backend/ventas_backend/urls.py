from django.urls import path
from .views import (
    create_empleado, read_empleado, update_empleado, delete_empleado,
    create_cliente, read_cliente, update_cliente, delete_cliente,
    procesar_pago_view, comprobante_boleta
)

urlpatterns = [
    path('api/empleados/create/', create_empleado, name='create_empleado'),
    path('api/empleados/read/<str:run>/', read_empleado, name='read_empleado'),
    path('api/empleados/update/<str:run>/', update_empleado, name='update_empleado'),
    path('api/empleados/delete/<str:run>/', delete_empleado, name='delete_empleado'),
    path('api/clientes/create/', create_cliente, name='create_cliente'),
    path('api/clientes/read/<str:rut>/', read_cliente, name='read_cliente'),
    path('api/clientes/update/<str:rut>/', update_cliente, name='update_cliente'),
    path('api/clientes/delete/<str:rut>/', delete_cliente, name='delete_cliente'),
    path('api/procesar_pago/', procesar_pago_view, name='procesar_pago'),
    path('api/comprobante/<int:pedido_id>/', comprobante_boleta, name='comprobante_boleta'),
]
