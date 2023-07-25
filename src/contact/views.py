from django.shortcuts import render
from django.core.mail import send_mail
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
        from_email = 'tchaco.soporte@gmail.com'  # Cambia por tu dirección de correo electrónico
        recipient_list = ['tchaco.soporte@gmail.com']  # Cambia por la dirección de correo del destinatario
        send_mail(subject, message, from_email, recipient_list)

    return render(request, 'core/contact.html', {})