# Generated by Django 4.2.3 on 2023-08-02 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='asunto',
            field=models.CharField(default='Asunto', max_length=200),
        ),
        migrations.AddField(
            model_name='contacto',
            name='tipo_consulta',
            field=models.CharField(choices=[('pregunta_general', 'Pregunta general'), ('sugerencia', 'Sugerencia'), ('reportar_problema', 'Reportar un problema')], default='Tipo Consulta', max_length=50),
        ),
    ]
