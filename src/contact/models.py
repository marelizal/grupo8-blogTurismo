from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    tipo_consulta = models.CharField(max_length=50, choices=[
        ('pregunta_general', 'Pregunta general'),
        ('sugerencia', 'Sugerencia'),
        ('reportar_problema', 'Reportar un problema')
    ])
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
