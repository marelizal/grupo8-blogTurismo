from django.db import models
from usuarios.models import Usuario
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    activo = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    activo = models.BooleanField(default=True)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    titulo = models.CharField(max_length=250)
    bajada = models.CharField(max_length=600)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='articulo', null=True)
    publicado = models.BooleanField(default=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, related_name='posteos', null=True)
    autor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, related_name='posteos_usario', null=True)
    etiqueta = models.ManyToManyField(Etiqueta)
    creacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)
    meGusta = models.ManyToManyField(Usuario, related_name='publicaciones_gustadas', blank=True)

    class Meta:
        ordering = ['-creacion']

    def __str__(self):
        return self.titulo

class Comment(models.Model):
    post = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    content = models.TextField()
    creacion = models.DateTimeField(auto_now_add=True)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.post.titulo}"