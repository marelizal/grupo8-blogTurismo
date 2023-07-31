from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from .models import Usuario

# Clase que crea un formulario
class RegistrarseForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2', 'email', 'telefono', 'domicilio']

        labels = {
            'first_name': 'Nombre', 
            'last_name': 'Apellido', 
            'username': 'Usuario', 
            'telefono': 'Teléfono', 
            'domicilio': 'Domicilio',
        }


class UsuarioForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'telefono', 'domicilio']
        labels = {
            'first_name': 'Nombre', 
            'last_name': 'Apellido', 
            'email': 'Correo electrónico', 
            'telefono': 'Teléfono', 
            'domicilio': 'Domicilio',
        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password'].widget = forms.HiddenInput()