# Generated by Django 4.2.6 on 2023-12-15 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensores', '0010_alter_datosdispositivo_dispositivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosdispositivo',
            name='dispositivo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='datos_dispositivos', to='sensores.usuarioarduino'),
        ),
    ]
