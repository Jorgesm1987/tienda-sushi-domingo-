# Instala
pip install Django
pip install djangorestframework
pip install djangorestframework_simplejwt
pip install pillow
pip install spyne
pip install lxml
pip install suds
pip install requests

# Crear el proyecto principal
django-admin startproject a_PROYECTO_TIENDA
cd a_PROYECTO_TIENDA

# Crear el proyecto backend
django-admin startproject backend

# Crear el proyecto frontend
django-admin startproject frontend

# Crear la aplicación de ventas dentro del backend
cd backend
django-admin startapp ventas_backend

# Volver al directorio del proyecto principal
cd ..

# Crear la aplicación de ventas dentro del frontend
cd frontend
django-admin startapp ventas_frontend

mkdir -p ventas_frontend/templates
mkdir -p ventas_frontend/static

# Volver al directorio del backend y aplicar migraciones
cd ..
cd backend
python manage.py makemigrations
python manage.py migrate


