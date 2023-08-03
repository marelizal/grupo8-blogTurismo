from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView 
from .views import RegistroView,editar_perfil,password_reset_view,password_reset_done_view,password_reset_confirm_view,password_reset_complete_view

app_name = 'usuarios'

urlpatterns = [
    path('login/', LoginView.as_view(template_name = 'usuarios/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(next_page = 'usuarios:login'), name = 'logout'),
    path('registrarse/', RegistroView.as_view(), name='registrarse'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),

    path('reset_password/', password_reset_view, name='password_reset'),
    path('reset_password/done/', password_reset_done_view, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', password_reset_confirm_view, name='password_reset_confirm'),
    path('reset/done/', password_reset_complete_view, name='password_reset_complete')
]