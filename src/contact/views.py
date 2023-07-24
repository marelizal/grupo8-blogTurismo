from django.shortcuts import render
from .models import Contacto
# Create your views here.

def contactoView(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        contact = Contacto(nombre=nombre, email=email, mensaje=mensaje)
        contact.save()

    return render(request, 'core/contact.html', {})