# Generated by Django 4.2.6 on 2023-12-23 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensores', '0014_alter_datosdispositivo_dispositivo_datos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DatosDispositivo',
        ),
    ]
