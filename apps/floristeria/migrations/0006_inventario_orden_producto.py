# Generated by Django 3.1.2 on 2020-11-03 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('floristeria', '0005_auto_20201030_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='orden_producto',
            fields=[
                ('id_producto_orden', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_inventario', models.AutoField(primary_key=True, serialize=False)),
                ('id_unidades_disponibles', models.SmallIntegerField()),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floristeria.producto')),
                ('id_sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floristeria.sede')),
            ],
        ),
    ]