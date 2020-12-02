from django import forms
from apps.floristeria.models import Producto, Categoria


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            'id_producto',
            'nombre_producto',
            'valor_base',
            'id_administrador'
        ]

        widgets = {
            'id_producto': forms.TextInput(),
            'nombre_producto': forms.TextInput(),
            'valor_base': forms.TextInput(),
            'id_administrador': forms.TextInput(),
            'genero': forms.TextInput(),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = [
            'id_categoria',
            'nombre_categoria'
        ]

        widgets = {
            'id_categoria': forms.NumberInput(),
            'nombre_categoria': forms.TextInput()
        }
