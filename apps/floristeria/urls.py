from django.urls import path
from apps.floristeria.views import index, registrarCategoria, login_redirect
from apps.floristeria.views import consultarProductos, registrarCliente
from apps.floristeria.views import crearProductos, eliminarProducto, editarProducto

urlpatterns = [
    path('', index, name='index'),
    path('consultarProductos', consultarProductos, name='consultarProductos'),
    path('crearProductos', crearProductos, name='crearProductos'),
    path('eliminarProducto/<id_prod>', eliminarProducto, name="eliminarProducto"),
    path('editarProducto/<id_prod>', editarProducto, name="editarProducto"),

    path('login_redirect', login_redirect),

    path('crearCategoria', registrarCategoria, name='crearCategoria'),
    path('registro', registrarCliente)
]
