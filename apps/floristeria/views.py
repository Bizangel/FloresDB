
from django.shortcuts import render
from django.http import HttpResponse

from apps.floristeria.models import Categoria, Producto
from apps.floristeria.forms import CategoriaForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.


def index(request):
    # Dependiendo del usuario redirigirlo propiamente
    if request.user.groups.filter(name="Administrador").exists():
        return consultarProductos(request)
    else:
        return render(request, 'floristeria/inicio.html')


def registrarCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        form.save()
        # return None
    else:
        form = CategoriaForm()
    return render(request, 'floristeria/formulario.html', {'form': form})


def consultarCategoria(request):
    Categorias = Categoria.objects.all()
    contexto = {'categorias': Categorias}
    return render(request, 'floristeria/consultar.html', contexto)


@login_required
def consultarProductos(request):
    if request.user.groups.filter(name="Administrador").exists():
        Productos = Producto.objects.all()
        administradores = User.objects.filter(groups__name='Administrador')
        administrador = administradores[0]
        contexto = {'productos': Productos, 'administrador': administrador}
        return render(request, 'floristeria/consultarProductos.html', contexto)
    else:
        return render(request, 'index.html', contexto)  # Al login
