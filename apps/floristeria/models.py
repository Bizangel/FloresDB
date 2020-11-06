from django.db import models
from django.contrib import admin
# Create your models here.


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)


class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)


class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    contrasena = models.CharField(max_length=45)
    id_sede = models.ForeignKey(Sede, on_delete=models.CASCADE)


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=45)
    valor_base = models.IntegerField()
    id_administrador = models.ForeignKey(Administrador,
                                         on_delete=models.CASCADE)


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=45)


class categoria_producto(models.Model):
    id_categoria_producto = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria,
                                     on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)


class Domiciliario(models.Model):
    id_domiciliario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    clave = models.CharField(max_length=45)


class Orden(models.Model):
    id_orden = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=45)
    fecha = models.DateField()
    hora = models.TimeField()
    notas = models.CharField(max_length=255)

    id_sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    id_domiciliario = models.ForeignKey(Domiciliario, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    valor_total = models.IntegerField()
    valor_domicilio = models.SmallIntegerField()
    id_orden = models.OneToOneField(Orden, on_delete=models.CASCADE)


class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)

    id_unidades_disponibles = models.SmallIntegerField()

    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_sede = models.ForeignKey(Sede, on_delete=models.CASCADE)


class orden_producto(models.Model):
    id_producto_orden = models.AutoField(primary_key=True)
