# Generated by Django 3.1.2 on 2020-12-02 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floristeria', '0003_administrador_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='username',
            field=models.CharField(default='NA', max_length=45),
        ),
        migrations.AddField(
            model_name='domiciliario',
            name='username',
            field=models.CharField(default='NA', max_length=45),
        ),
    ]