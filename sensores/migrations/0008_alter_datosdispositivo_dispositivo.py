# Generated by Django 4.2.6 on 2023-12-11 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensores', '0007_alter_datosdispositivo_dispositivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosdispositivo',
            name='dispositivo',
            field=models.CharField(max_length=50),
        ),
    ]