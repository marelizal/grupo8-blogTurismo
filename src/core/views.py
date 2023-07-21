from django.shortcuts import render
from posts.models import Categoria,Articulo

# vista de la pagina de inicio


def indexView(request):
    # Obtener las últimas publicaciones
    ultimas_publicaciones = Articulo.objects.filter(publicado=True)[:5]

    # Obtener todas las categorías y etiquetas
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
