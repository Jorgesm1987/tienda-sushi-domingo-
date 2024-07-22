from django.db import models

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'clientes'

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    run = models.CharField(max_length=10)
    nombres = models.CharField(max_length=100)
    ap_paterno = models.CharField(max_length=100)
    ap_materno = models.CharField(max_length=100)
    email = models.EmailField()
    genero = models.CharField(max_length=10)
    region = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)

    class Meta:
        db_table = 'empleados'

    def __str__(self):
        return f'{self.nombres} {self.ap_paterno} {self.ap_materno}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.ManyToManyField(Categoria, related_name='productos')
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    class Meta:
        db_table = 'productos'

    def __str__(self):
        return self.nombre

class Direccion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='direcciones')
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)

    class Meta:
        db_table = 'direcciones'

    def __str__(self):
        return f'{self.direccion}, {self.ciudad}, {self.region}, {self.pais}'

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True, blank=True, related_name='pedidos')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    direccion_entrega = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True, blank=True, related_name='pedidos')

    class Meta:
        db_table = 'pedidos'

    def __str__(self):
        return f'Pedido {self.id} de {self.cliente.nombre}'

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'detalle_pedidos'

    def __str__(self):
        return f'{self.cantidad} x {self.producto.nombre}'

class Carrito(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='carrito')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'carrito'

    def __str__(self):
        return f'Carrito de {self.cliente.nombre}'

class CarritoProducto(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='carrito_productos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    class Meta:
        db_table = 'carrito_producto'

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre}'

class Pago(models.Model):
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='pago')
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    metodo_pago = models.CharField(max_length=50)


    class Meta:
        db_table = 'pagos'

    def __str__(self):
        return f'Pago de {self.monto} para el pedido {self.pedido.id}'

