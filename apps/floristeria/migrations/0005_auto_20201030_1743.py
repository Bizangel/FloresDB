# Generated by Django 3.1.2 on 2020-10-30 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('floristeria', '0004_cliente_factura_orden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='id_orden',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='floristeria.orden'),
        ),
    ]
