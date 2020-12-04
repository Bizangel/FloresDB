
from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.floristeria.models import Categoria, Producto, Administrador, Sede
from apps.floristeria.models import categoria_producto, Domiciliario, Cliente
from apps.floristeria.models import carrito_producto, Carrito
from apps.floristeria.forms import CategoriaForm, ProductoForm, ClienteForm
from apps.floristeria.forms import DomiciliarioForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth.models import Group as DjangoGroup

# from django.contrib.auth.hashers import make_password
from django.contrib import messages
# Create your views here.


def index(request):
    # Dependiendo del usuario redirigirlo propiament
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})


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


# Domiciliarios
@login_required
def registrarDomiciliario(request):
    if request.user.groups.filter(name="Administrador").exists():
        if request.method == 'POST':
            form = DomiciliarioForm(request.POST)

            if form.is_valid():
                sedeNombre = form.cleaned_data['sede']
                sede = Sede.objects.get(nombre=sedeNombre)

                search = DjangoUser.objects.filter(
                    username=form.cleaned_data['username'])
                if len(search) > 0:  # Ya existe
                    contexto = {'form': form}
                    messages.error(request, 'Ese nombre de usuario ya esta en uso')
                    return render(request, 'floristeria/registrarDomiciliario.html', contexto)

                form = form.save(commit=False)
                nuevoCliente = DjangoUser.objects.create_user(
                    form.username, form.correo, form.contrasena)

                clientes = DjangoGroup.objects.get(name='Domiciliario')
                clientes.user_set.add(nuevoCliente)

                form.id_sede = sede
                form.contrasena = '.'  # Remove pass
                form.save()

                return redirect('consultarDomiciliarios')
            else:

                form = DomiciliarioForm()
                contexto = {'form': form}
                return render(request, 'floristeria/registrarDomiciliario.html', contexto)

        else:
            form = DomiciliarioForm()
            contexto = {'form': form}
            return render(request, 'floristeria/registrarDomiciliario.html', contexto)


@login_required
def editarDomiciliario(request, id_dom):
    if request.user.groups.filter(name="Administrador").exists():
        domici = Domiciliario.objects.get(id_domiciliario=id_dom)
        if request.method == 'POST':
            form = DomiciliarioForm(request.POST, instance=domici)
            if form.is_valid():
                sedeNombre = form.cleaned_data['sede']
                sede = Sede.objects.get(nombre=sedeNombre)

                form = form.save(commit=False)  # new form instance
                form.id_sede = sede
                form.save()
                return redirect('consultarDomiciliarios')
            else:
                print('invalid')

        form = DomiciliarioForm(instance=domici)
        form.fields.pop('username')
        form.fields.pop('contrasena')

        contexto = {'form': form}
        return render(request, 'floristeria/editarDomiciliario.html', contexto)
    else:
        return redirect('index')  # Al login


@login_required
def consultarDomiciliarios(request):

    if request.user.groups.filter(name="Administrador").exists():
        # Productos = Producto.objects.order_by('-id_producto') #descendiente
        domiciliarios = Domiciliario.objects.order_by('id_domiciliario')  # ascendiente

        consultar = True
        contexto = {'domiciliarios': domiciliarios, 'consultar': consultar}

        return render(request, 'floristeria/consultarDomiciliarios.html', contexto)
    else:
        return redirect('index')  # Al login


# Carritos

@login_required
def consultarCarrito(request):
    if request.user.groups.filter(name="Cliente").exists():
        cliente = Cliente.objects.get(username=request.user.username)

        if len(Carrito.objects.filter(id_cliente=cliente)) == 0:
            # Create carrito
            carrito = Carrito(valor_total=0, id_cliente=cliente)
            carrito.save()
        else:
            carrito = Carrito.objects.get(id_cliente=cliente)

        carrito_productos = carrito_producto.objects.filter(id_carrito=carrito)

        consultar = True
        contexto = {'carrito_productos': carrito_productos, 'consultar': consultar}

        return render(request, 'floristeria/consultarCarrito.html', contexto)
    else:
        return redirect('index')  # Al login
