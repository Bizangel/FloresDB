# Generated by Django 3.1.2 on 2020-11-09 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floristeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrador',
            name='correo',
            field=models.CharField(default='nice', max_length=45),
            preserve_default=False,
        ),
    ]
