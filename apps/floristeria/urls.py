from django.urls import path
from apps.floristeria.views import index, registrarCategoria
from apps.floristeria.views import consultarCategoria, consultarProductos

urlpatterns = [
    path('', index),

    path('consultarProductos', consultarProductos)
]
