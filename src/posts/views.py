
from django.shortcuts import render, redirect,get_object_or_404
from .forms import ArticuloForm
from .models import Articulo, Categoria


def post_list(request):
    post = Articulo.objects.all()
    categorias = Categoria.objects.all()

    context = {
        'posts': post,
        "categorias": categorias
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