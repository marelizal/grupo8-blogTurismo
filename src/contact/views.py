from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contacto
# Create your views here.

def contactoView(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        mensaje = request.POST.get('mensaje')
        contact = Contacto(nombre=nombre, email=email, mensaje=mensaje)
        contact.save()

        # Enviar correo electrónico
        subject = 'Nuevo mensaje de contacto'
        message = f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}'
        from_email = 'tchaco.soporte@gmail.com'
        recipient_list = ['tchaco.soporte@gmail.com']
        send_mail(subject, message, from_email, recipient_list)

          # Mostrar mensaje flash
        messages.success(request, 'El mensaje se envió correctamente. ¡Gracias por contactarnos!')
        return redirect('contacto')  # Redireccionar a la misma página para mostrar la alerta

    return render(request, 'core/contact.html', {})