# Generated by Django 3.1.2 on 2020-10-30 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Sede',
            fields=[
                ('id_sede', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('id_ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floristeria.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_administrador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('contrasena', models.CharField(max_length=45)),
                ('id_sede', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floristeria.sede')),
            ],
        ),
    ]
