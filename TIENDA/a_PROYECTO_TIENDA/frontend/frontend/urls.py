from django.contrib import admin
from django.urls import path
from ventas_frontend import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('empleados/', views.empleados, name='empleados'),
    path('clientes/', views.clientes, name='clientes'),
    path('productos/', views.productos, name='productos'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('login/', views.login, name='login'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('carrito/', views.carrito, name='carrito'),
    path('home/', views.home, name='home'),
]


