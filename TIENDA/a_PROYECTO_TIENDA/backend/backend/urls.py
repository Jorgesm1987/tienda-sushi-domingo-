# backend/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ventas_backend.urls')),  # Asegúrate de incluir las URLs de ventas_backend
]




