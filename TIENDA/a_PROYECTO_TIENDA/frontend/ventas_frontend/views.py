from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def empleados(request):
    return render(request, 'empleados.html')

def clientes(request):
    return render(request, 'clientes.html')

def productos(request):
    return render(request, 'productos.html')

def ofertas(request):
    return render(request, 'ofertas.html')

def login(request):
    return render(request, 'login.html')

def catalogo(request):
    return render(request, 'catalogo.html')

def carrito(request):
    return render(request, 'carrito.html')

def comprobante(request):
    return render(request, 'comprobante.html')
