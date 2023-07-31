from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contacto

def contactoView(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        tipo_consulta = request.POST.get('tipo_consulta')
        mensaje = request.POST.get('mensaje')

        # Enviar correo electrónico
        subject = f'Nuevo mensaje de contacto - {asunto}'
        message = f'Nombre: {nombre}\nEmail: {email}\nTipo de consulta: {tipo_consulta}\nMensaje: {mensaje}'
        from_email = 'tchaco.soporte@gmail.com'
        recipient_list = ['tchaco.soporte@gmail.com']
        send_mail(subject, message, from_email, recipient_list)

        # Mostrar mensaje de éxito
        messages.success(request, 'El mensaje se envió correctamente. ¡Gracias por contactarnos!')
        return redirect('contacto')

    return render(request, 'core/contact.html', {})
