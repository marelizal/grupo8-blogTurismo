from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Articulo,Categoria

def post_list(request):
    post = Articulo.objects.all()
    categorias = Categoria.objects.all()

    context = {
        'posts': post,
        "categorias":categorias
    }
    return render(request, 'posts/post_list.html', context)

def post_detail(request, pk):
    post = Articulo.objects.get(pk=pk)
    categorias = Categoria.objects.all()

    context = {
        "post": post,  
        "categorias": categorias
    }
    return render(request, 'posts/post_detail.html', context)
