from django.shortcuts import render

# Create your views here.

# vista de la pagina de inicio
def indexView(request):
    return render(request, 'index.html', {})

def aboutView(request):
    return render(request, 'about.html', {})

def contactView(request):
    return render(request, 'contact.html', {})