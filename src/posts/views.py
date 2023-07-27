
from django.shortcuts import render, redirect,get_object_or_404
from .forms import ArticuloForm,CommentForm
from .models import Articulo, Categoria,Comment 
from django.views.generic import ListView
from django.utils import timezone



def post_list(request):
    queryset = Articulo.objects.all()
    categorias = Categoria.objects.all()

    categoria_seleccionada = request.GET.get('categoria')
    if categoria_seleccionada:
        queryset = queryset.filter(categoria__nombre=categoria_seleccionada)

    orden = request.GET.get('orderby')
    if orden == 'fecha_asc':
        queryset = queryset.order_by('fecha')

    context = {
        'posts': queryset,
        'categorias': categorias,
        'categoria_seleccionada': categoria_seleccionada,
        'orden': orden, 
    }

    return render(request, 'posts/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Articulo, pk=pk)
    categorias = Categoria.objects.all()
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.autor = request.user
            comment.fecha = timezone.now()  # Agregar la fecha actual al comentario
            comment.save()
            return redirect('post_detail', pk=post.pk)

    context = {
        "post": post,
        "categorias": categorias,
        "comment_form": comment_form,
    }
    return render(request, 'posts/post_detail.html', context)




    

    

def post_add(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user  
            articulo.save()
            return redirect('post_detail', pk=articulo.pk)
    else:
        form = ArticuloForm()
    
    return render(request, 'posts/post_add.html', {'form': form})



def post_update(request, post_id):
    articulo = get_object_or_404(Articulo, pk=post_id)

    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=articulo)
        if form.is_valid():
            form.save()
            return redirect('post_list') 
    else:
        form = ArticuloForm(instance=articulo)

    return render(request, 'posts/post_update.html', {'form': form})

def post_delete(request, post_id):
    articulo = get_object_or_404(Articulo, pk=post_id)

    if request.method == 'POST':
        articulo.delete()
        return redirect('post_list')


    return render(request, 'posts/post_confirm_delete.html', {'post': articulo})