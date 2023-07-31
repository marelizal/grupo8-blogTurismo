from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import RegistrarseForm,UsuarioForm
from django.urls import reverse
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.

# Vista basada en clases que crea un usuario
class RegistroView(CreateView):
    model = Usuario
    template_name = 'usuarios/registro.html'
    form_class = RegistrarseForm

    def get_success_url(self):
        return reverse('index')
    

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response
    

def editar_perfil(request):
    usuario_actual = request.user

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario_actual)

        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect(reverse('usuarios:editar_perfil'))  

    else:
        form = UsuarioForm(instance=usuario_actual)

    return render(request, 'usuarios/editar_perfil.html', {'form': form})