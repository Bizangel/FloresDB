
from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.floristeria.models import Categoria, Producto, Administrador
from apps.floristeria.models import categoria_producto
from apps.floristeria.forms import CategoriaForm, ProductoForm, ClienteForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.models import Group as DjangoGroup

# from django.contrib.auth.hashers import make_password
from django.contrib import messages
# Create your views here.


def index(request):
    # Dependiendo del usuario redirigirlo propiament
    return render(request, 'index.html')


@login_required
def login_redirect(request):
    if request.user.groups.filter(name="Administrador").exists():
        return redirect('consultarProductos')
    else:
        return redirect('index')


def registrarCategoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('consultarProductos')
    else:
        form = CategoriaForm()
    return render(request, 'floristeria/crearCategoria.html', {'form': form})


def registrarCliente(request):

    if request.user.is_authenticated:
        return index(request)

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():

            search = DjangoUser.objects.filter(
                username=form.cleaned_data['username'])
            if len(search) > 0:  # Ya existe
                contexto = {'form': form}
                messages.error(request, 'Ese nombre de usuario ya esta en uso')
                return render(request, 'floristeria/registro.html', contexto)

            form = form.save(commit=False)
            nuevoCliente = DjangoUser.objects.create_user(
                form.username, form.correo, form.clave)

            clientes = DjangoGroup.objects.get(name='Cliente')
            clientes.user_set.add(nuevoCliente)

            form.clave = '.'  # Remove pass
            form.save()

            return login_redirect(request)
        else:

            form = ClienteForm()
            contexto = {'form': form}
            return render(request, 'floristeria/registro.html', contexto)

    else:
        form = ClienteForm()
        contexto = {'form': form}
        return render(request, 'floristeria/registro.html', contexto)


@login_required
def editarProducto(request, id_prod):
    if request.user.groups.filter(name="Administrador").exists():
        producto = Producto.objects.get(id_producto=id_prod)
        if request.method == 'POST':
            form = ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                categoria = form.cleaned_data['categoria']

                form = form.save(commit=False)  # new form instance

                form.save()

                # Crearle la categoria_producto
                cat = Categoria.objects.get(
                    nombre_categoria=categoria)

                catprog = categoria_producto.objects.get(
                    id_producto=form.id_producto)
                catprog.id_categoria = cat
                # print('not read')
                catprog.save()
                return redirect('consultarProductos')

        form = ProductoForm(instance=producto)

        contexto = {'form': form}
        return render(request, 'floristeria/editarProducto.html', contexto)
    else:
        return redirect('index')  # Al login


@login_required
def consultarProductos(request):
    if request.user.groups.filter(name="Administrador").exists():
        # Productos = Producto.objects.order_by('-id_producto') #descendiente
        Productos = Producto.objects.order_by('id_producto')  # ascendiente

        consultar = True
        contexto = {'productos': Productos, 'consultar': consultar}
        return render(request, 'floristeria/consultarProductos.html', contexto)
    else:
        return redirect('index')  # Al login


@login_required
def eliminarProducto(request, id_prod):
    if request.method == 'POST':
        producto = Producto.objects.get(id_producto=id_prod)
        catprog = categoria_producto.objects.get(
            id_producto=producto.id_producto)
        producto.delete()
        catprog.delete()
        return redirect('consultarProductos')


@login_required
def crearProductos(request):
    crear = True
    if request.user.groups.filter(name="Administrador").exists():
        if request.method == 'POST':
            form = ProductoForm(request.POST)

            if form.is_valid():
                categoria = form.cleaned_data['categoria']

                form = form.save(commit=False)  # new form instance
                admin = Administrador.objects.get(username=request.user.username)
                form.id_administrador = admin

                form.save()

                # Crearle la categoria_producto
                cat = Categoria.objects.get(
                    nombre_categoria=categoria)

                catprog = categoria_producto.objects.create(
                    id_categoria=cat, id_producto=form)
                catprog.save()

                messages.success(request, 'Éxito registrando el producto')
                form = ProductoForm()

                return render(request, 'floristeria/crearProductos.html',
                              {'form': form, 'crear': crear})

        form = ProductoForm()
        return render(request, 'floristeria/crearProductos.html',
                      {'form': form, 'crear': crear})
    else:
        return index(request)
