from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView
from .models import Usuario
from .forms import RegistrarseForm,UsuarioForm
from django.urls import reverse
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import views as auth_views


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


def password_reset_view(request):
    if request.method == 'POST':
        form = auth_views.PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                from_email='tchaco.soporte@gmail.com',  
                email_template_name='usuarios/password_reset_email.html', 
            )
            messages.success(request, 'Se ha enviado un correo electrónico con instrucciones para restablecer tu contraseña.')
            return redirect('usuarios:password_reset_done')
    else:
        form = auth_views.PasswordResetForm()
    return render(request, 'usuarios/password_reset.html', {'form': form})


def password_reset_done_view(request):
    return render(request, 'usuarios/password_reset_done.html')


def password_reset_confirm_view(request, uidb64, token):
    return auth_views.PasswordResetConfirmView.as_view(
        template_name='usuarios/password_reset_confirm.html',
        success_url=reverse('usuarios:password_reset_complete')
    )(request, uidb64=uidb64, token=token)

def password_reset_complete_view(request):
    return render(request, 'usuarios/password_reset_complete.html')