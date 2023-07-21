from django.urls import path, include
from core import views  

#app_name = 'core'


urlpatterns = [
    path('', views.indexView, name = 'index'),
    path('acerca_de_nosotros', views.aboutView, name = 'about'),
    path('contacto', views.contactView, name = 'contact'),

    # includes
    # path('noticias/', include('noticias.urls')),
    # path('usuarios/', include('usuarios.urls')),
]  