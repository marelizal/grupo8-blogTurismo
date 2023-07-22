import os
from django.conf import settings
from django.shortcuts import get_object_or_404, render, redirect, reverse
from posts.models import Categoria,Articulo

# vista de la pagina de inicio


def indexView(request):
    # Obtener las últimas publicaciones
    ultimas_publicaciones = Articulo.objects.filter(publicado=True)[:5]

    # Obtener todas las categorías
    categorias = Categoria.objects.all()

    # Pasar los datos como contexto al renderizado de la plantilla
    context = {
        'ultimas_publicaciones': ultimas_publicaciones,
        'categorias': categorias,
    }

    return render(request, 'core/index.html', context)



def aboutView(request):
    return render(request, 'core/about.html', {})


def contactView(request):
    return render(request, 'core/contact.html', {})

def galleryView(request):
    media_path = os.path.join(settings.MEDIA_ROOT,'articulo')  # Obtiene la ruta absoluta de la carpeta /media
    image_files = [f for f in os.listdir(media_path) if os.path.isfile(os.path.join(media_path, f))]
    images = [os.path.join(settings.MEDIA_URL, 'articulo', f) for f in image_files]
    return render(request, 'core/gallery.html', {'images': images})
