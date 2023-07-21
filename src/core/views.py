from django.shortcuts import render

# Create your views here.

# vista de la pagina de inicio
def indexView(request):
    return render(request, 'core/index.html', {})

def aboutView(request):
    return render(request, 'core/about.html', {})

def contactView(request):
    return render(request, 'core/contact.html', {})