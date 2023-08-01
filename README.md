# Proyecto Final del Informatorio 2023 Grupo 8
Repositorio para el Proyecto

# README - Aplicación de Turismo

## Descripción 
Esta es una aplicación web de turismo desarrollada en Django que tiene como objetivo proporcionar información sobre destinos turísticos, atracciones y actividades en diferentes lugares. Los usuarios pueden registrarse, iniciar sesión y explorar una amplia gama de destinos turísticos, ver detalles sobre cada lugar, agregar comentarios y publicaciones.

## Características principales 📋
- Registro de usuarios: Los usuarios pueden crear una cuenta y acceder a la plataforma.
- Inicio de sesión: Los usuarios registrados pueden iniciar sesión en la aplicación.
- Detalles de las publicaciones: Los usuarios pueden hacer clic en las publicaciones para ver más información, imágenes y comentarios.
- Agregar reaccion y comentarios: Los usuarios pueden agregar comentarios y reaccionar a las destintas publicaciones.
- Administración: Los administradores pueden acceder al panel de administración de Django para gestionar, crear, modificar y eliminar usuarios.

## Requisitos del sistema 🛠️
- Python 3.x  Del lado del servidor (backend)
- Django 3.x  Framework web
- PostgreSQL (u otro motor de base de datos compatible con Django)
- Bootstrap(https://getbootstrap.com/) Framework web para el desarrollo frontend (HTML, CSS, JavaScript)
- Otros requisitos específicos que se encuentren en el archivo `requirements.txt`.


## Instalación 🔧
1. Clonar el repositorio:

```
git clone https://github.com/marelizal/grupo8-blogTurismo.git
cd grupo8-blogTurismo
```

2. Crear un entorno virtual e instalar las dependencias:

```
python -m venv ve_blogTurismo
source ve_blogTurismo/bin/activate  # En Windows: ve_blogTurismo\Scripts\activate
pip install -r requirements.txt
```

3. Configurar la base de datos en el archivo `settings`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_basedatos',
        'USER': 'nombre_usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': 'porDefecto',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tchaco.soporte@gmail.com'
EMAIL_HOST_PASSWORD = 'cvnhujdgwhqjqdrj'
```

4. Realizar las migraciones de la base de datos:

```
python manage.py makemigrations

python manage.py migrate
```

5. Crear un superusuario para acceder al panel de administración:

```
python manage.py createsuperuser
```

6. Iniciar el servidor de desarrollo:

```
python manage.py runserver
```

7. Acceder a la aplicación en tu navegador web en la dirección `http://localhost:8000/`.


