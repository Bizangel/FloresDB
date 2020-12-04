from django import forms
from apps.floristeria.models import Producto, Categoria, Administrador, Sede
from apps.floristeria.models import categoria_producto, Cliente, Domiciliario

GEEKS_CHOICES = (
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)
#
# forms.


class ProductoForm(forms.ModelForm):
    # id_administrador = forms.ChoiceField(
    #     choices=[(admin.username, admin.username) for admin in Administrador.objects.all()])
    # categoria = forms.CharField(attrs={'class': 'form-control'})

    categoria = forms.ChoiceField(
        choices=[(cat.nombre_categoria, cat.nombre_categoria) for cat in Categoria.objects.all()])

    class Meta:
        model = Producto
        fields = [
            'nombre_producto',
            'valor_base'
        ]

        # exclude = ['id_administrador', ]  # Sera proveido posteriormente

        widgets = {
            'nombre_producto': forms.TextInput(),
            'valor_base': forms.NumberInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        # Le asigna el estilo de bootstrap
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'apellido',
            'celular',
            'correo',
            'username',
            'clave'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'celular': forms.NumberInput(attrs={'placeholder': 'Celular'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'ejemplo@gmail.com'}),
            'username': forms.TextInput(attrs={'placeholder': 'Usuario'}),
            'clave': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        # Le asigna el estilo de bootstrap
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class DomiciliarioForm(forms.ModelForm):
    sede = forms.ChoiceField(
        choices=[(sed.nombre, sed.nombre) for sed in Sede.objects.all()])

    class Meta:
        model = Domiciliario
        fields = [
            'nombre',
            'apellido',
            'correo',
            'username',
            'contrasena'
        ]

        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'placeholder': 'Apellido'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'ejemplo@gmail.com'}),
            'username': forms.TextInput(attrs={'placeholder': 'Usuario'}),
            'contrasena': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(DomiciliarioForm, self).__init__(*args, **kwargs)
        # Le asigna el estilo de bootstrap
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = [
            'id_categoria',
            'nombre_categoria'
        ]

        widgets = {
            'id_categoria': forms.NumberInput(),
            'nombre_categoria': forms.TextInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)
        # Le asigna el estilo de bootstrap
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
