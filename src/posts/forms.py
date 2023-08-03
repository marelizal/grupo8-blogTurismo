from django import forms
from .models import Articulo, Comment, Categoria, Etiqueta


class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        exclude = ['autor','bajada']

        fields = ['titulo', 'bajada', 'contenido', 'imagen',
                  'publicado', 'categoria', 'etiqueta', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'bajada': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'publicado': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'etiqueta': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'autor': forms.Select(attrs={'class': 'form-select'}),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 5:
            raise forms.ValidationError(
                'El título debe tener al menos 5 caracteres.')
        return titulo

    def clean_contenido(self):
        contenido = self.cleaned_data.get('contenido')
        if len(contenido) < 50:
            raise forms.ValidationError(
                'El contenido debe tener al menos 50 caracteres.')
        return contenido

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if imagen:
            # Validar el tamaño de la imagen si es necesario
            if imagen.size > 5 * 1024 * 1024:  # 5 MB
                raise forms.ValidationError(
                    'El tamaño de la imagen no puede exceder los 5 MB.')
            # Validar el tipo de archivo si es necesario
            if not imagen.name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                raise forms.ValidationError(
                    'El formato de la imagen no es válido. Solo se permiten archivos JPG, JPEG, PNG y GIF.')
        return imagen


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': 'Deja tu comentario:',
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 100px;',
                'placeholder': 'Deja tu comentario para esta publicacion',
            }),

        }

class CrearCategoryForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        
class CrearTagForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre']        