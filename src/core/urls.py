from django.urls import path, include
from core import views  


#app_name = 'core'


urlpatterns = [
    path('', views.indexView, name = 'index'),
    path('acerca_de_nosotros', views.aboutView, name = 'about'),
    path('contacto', views.contactView, name = 'contact'),
    path('gallery', views.galleryView, name = 'gallery'),

    # Inclu
    path('publicaciones/', include('posts.urls')),
]  